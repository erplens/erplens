# -*- coding: utf-8 -*-

""" Modules (also called addons) management.

"""

from . import db, graph, loading, migration, module, registry

from openerp.modules.loading import load_modules

from openerp.modules.module import get_modules, get_modules_with_version, \
    load_information_from_description_file, get_module_resource, get_module_path, \
    initialize_sys_path, load_openerp_module, init_module_models, adapt_version

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
