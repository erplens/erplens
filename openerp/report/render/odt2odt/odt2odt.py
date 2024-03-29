# -*- coding: utf-8 -*-

from openerp.report.render.rml2pdf import utils
import copy

class odt2odt(object):
    def __init__(self, odt, localcontext):
        self.localcontext = localcontext
        self.etree = odt
        self._node = None

    def render(self):
        def process_text(node,new_node):
            for child in utils._child_get(node, self):
                new_child = copy.deepcopy(child)
                new_node.append(new_child)
                if len(child):
                    for n in new_child:
                        new_child.text  = utils._process_text(self, child.text)
                        new_child.tail  = utils._process_text(self, child.tail)
                        new_child.remove(n)
                    process_text(child, new_child)
                else:
                    new_child.text  = utils._process_text(self, child.text)
                    new_child.tail  = utils._process_text(self, child.tail)
        self._node = copy.deepcopy(self.etree)
        for n in self._node:
            self._node.remove(n)
        process_text(self.etree, self._node)
        return self._node

def parseNode(node, localcontext = {}):
    r = odt2odt(node, localcontext)
    return r.render()


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
