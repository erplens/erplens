# -*- coding: utf-8 -*-

import time

functions = {
    'today': lambda x: time.strftime('%d/%m/%Y', time.localtime()).decode('latin1')
}

#
# TODO: call an object internal function too
#
def print_fnc(fnc, arg):
    if fnc in functions:
        return functions[fnc](arg)
    return ''

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

