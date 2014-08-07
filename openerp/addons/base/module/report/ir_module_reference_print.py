# -*- coding: utf-8 -*-

import time

from openerp.report import report_sxw

class ir_module_reference_print(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(ir_module_reference_print, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time': time,
            'findobj': self._object_find,
            'objdoc': self._object_doc,
            'objdoc2': self._object_doc2,
            'findflds': self._fields_find,
        })
    def _object_doc(self, obj):
        modobj = self.pool[obj]
        strdocs= modobj.__doc__
        if not strdocs:
            return None
        else:
            strdocs=strdocs.strip().splitlines(True)
        res = ''
        for stre in strdocs:
            if not stre or stre.isspace():
                break
            res += stre
        return res

    def _object_doc2(self, obj):
        modobj = self.pool[obj]
        strdocs= modobj.__doc__
        if not strdocs:
            return None
        else:
            strdocs=strdocs.strip().splitlines(True)
        res = []
        fou = False
        for stre in strdocs:
            if fou:
                res.append(stre.strip())
            elif not stre or stre.isspace():
                fou = True
        return res

    def _object_find(self, module):
        ids2 = self.pool['ir.model.data'].search(self.cr, self.uid, [('module','=',module), ('model','=','ir.model')])
        ids = []
        for mod in self.pool['ir.model.data'].browse(self.cr, self.uid, ids2):
            ids.append(mod.res_id)
        modobj = self.pool['ir.model']
        return modobj.browse(self.cr, self.uid, ids)

    def _fields_find(self, obj, module):
        res = []
        data_obj = self.pool['ir.model.data']
        modobj = self.pool[obj]
        fname_wildcard = 'field_' + modobj._name.replace('.', '_') + '_%'
        module_fields_ids = data_obj.search(self.cr, self.uid, [('model', '=', 'ir.model.fields'), ('module', '=', module), ('name', 'like', fname_wildcard)])
        if module_fields_ids:
            module_fields_res_ids = [x['res_id'] for x in data_obj.read(self.cr, self.uid, module_fields_ids, ['res_id'])]
            module_fields_names = [x['name'] for x in self.pool['ir.model.fields'].read(self.cr, self.uid, module_fields_res_ids, ['name'])]
            res = modobj.fields_get(self.cr, self.uid, allfields=module_fields_names).items()
            res.sort()
        return res

report_sxw.report_sxw('report.ir.module.reference', 'ir.module.module',
        'addons/base/module/report/ir_module_reference.rml',
        parser=ir_module_reference_print, header=False)


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

