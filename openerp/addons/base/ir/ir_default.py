# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class ir_default(osv.osv):
    _name = 'ir.default'
    _columns = {
        'field_tbl': fields.char('Object'),
        'field_name': fields.char('Object Field'),
        'value': fields.char('Default Value'),
        'uid': fields.many2one('res.users', 'Users'),
        'page': fields.char('View'),
        'ref_table': fields.char('Table Ref.'),
        'ref_id': fields.integer('ID Ref.',size=64),
        'company_id': fields.many2one('res.company','Company')
    }

    def _get_company_id(self, cr, uid, context=None):
        res = self.pool.get('res.users').read(cr, uid, [uid], ['company_id'], context=context)
        if res and res[0]['company_id']:
            return res[0]['company_id'][0]
        return False

    _defaults = {
        'company_id': _get_company_id,
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
