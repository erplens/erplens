# -*- coding: utf-8 -*-

import openerp
import openerp.exceptions

def login(db, login, password):
    res_users = openerp.registry(db)['res.users']
    return res_users._login(db, login, password)

def check_super(passwd):
    if passwd == openerp.tools.config['admin_passwd']:
        return True
    else:
        raise openerp.exceptions.AccessDenied()

def check(db, uid, passwd):
    res_users = openerp.registry(db)['res.users']
    return res_users.check(db, uid, passwd)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
