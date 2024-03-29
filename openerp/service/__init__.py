# -*- coding: utf-8 -*-

import common
import db
import model
import report
import wsgi_server
import server

#.apidoc title: RPC Services

""" Classes of this module implement the network protocols that the
    OpenERP server uses to communicate with remote clients.

    Some classes are mostly utilities, whose API need not be visible to
    the average user/developer. Study them only if you are about to
    implement an extension to the network protocols, or need to debug some
    low-level behavior of the wire.
"""


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
