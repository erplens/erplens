# -*- coding: utf-8 -*-

import base64
import cStringIO

from openerp import tools
from openerp.osv import fields,osv
from openerp.tools.translate import _
from openerp.tools.misc import get_iso_codes

NEW_LANG_KEY = '__new__'

class base_language_export(osv.osv_memory):
    _name = "base.language.export"

    def _get_languages(self, cr, uid, context):
        lang_obj = self.pool.get('res.lang')
        ids = lang_obj.search(cr, uid, [('translatable', '=', True)])
        langs = lang_obj.browse(cr, uid, ids)
        return [(NEW_LANG_KEY, _('New Language (Empty translation template)'))] + [(lang.code, lang.name) for lang in langs]
   
    _columns = {
            'name': fields.char('File Name', readonly=True),
            'lang': fields.selection(_get_languages, 'Language', required=True), 
            'format': fields.selection([('csv','CSV File'),
                                        ('po','PO File'),
                                        ('tgz', 'TGZ Archive')], 'File Format', required=True),
            'modules': fields.many2many('ir.module.module', 'rel_modules_langexport', 'wiz_id', 'module_id', 'Modules To Export', domain=[('state','=','installed')]),
            'data': fields.binary('File', readonly=True),
            'state': fields.selection([('choose', 'choose'),   # choose language
                                       ('get', 'get')])        # get the file
    }
    _defaults = { 
        'state': 'choose',
        'name': 'lang.tar.gz',
        'lang': NEW_LANG_KEY,
        'format': 'csv',
    }

    def act_getfile(self, cr, uid, ids, context=None):
        this = self.browse(cr, uid, ids)[0]
        lang = this.lang if this.lang != NEW_LANG_KEY else False
        mods = map(lambda m: m.name, this.modules) or ['all']
        mods.sort()
        buf = cStringIO.StringIO()
        tools.trans_export(lang, mods, buf, this.format, cr)
        filename = 'new'
        if lang:
            filename = get_iso_codes(lang)
        elif len(mods) == 1:
            filename = mods[0]
        this.name = "%s.%s" % (filename, this.format)
        out = base64.encodestring(buf.getvalue())
        buf.close()
        self.write(cr, uid, ids, {'state': 'get',
                                  'data': out,
                                  'name':this.name}, context=context)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'base.language.export',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': this.id,
            'views': [(False, 'form')],
            'target': 'new',
        }


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
