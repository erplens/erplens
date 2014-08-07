# -*- coding: utf-8 -*-

from ..exceptions import except_orm
from .orm import Model, TransientModel, AbstractModel

# Deprecated, kept for backward compatibility.
# openerp.exceptions.Warning should be used instead.
except_osv = except_orm

# Deprecated, kept for backward compatibility.
osv = Model
osv_memory = TransientModel
osv_abstract = AbstractModel # ;-)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
