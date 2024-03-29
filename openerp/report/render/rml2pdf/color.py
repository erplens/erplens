# -*- coding: utf-8 -*-

from reportlab.lib import colors
import re

allcols = colors.getAllNamedColors()

regex_t = re.compile('\(([0-9\.]*),([0-9\.]*),([0-9\.]*)\)')
regex_h = re.compile('#([0-9a-zA-Z][0-9a-zA-Z])([0-9a-zA-Z][0-9a-zA-Z])([0-9a-zA-Z][0-9a-zA-Z])')

def get(col_str):
    if col_str is None:
        col_str = ''
    global allcols
    if col_str in allcols.keys():
        return allcols[col_str]
    res = regex_t.search(col_str, 0)
    if res:
        return float(res.group(1)), float(res.group(2)), float(res.group(3))
    res = regex_h.search(col_str, 0)
    if res:
        return tuple([ float(int(res.group(i),16))/255 for i in range(1,4)])
    return colors.red

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

