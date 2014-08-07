# -*- coding: utf-8 -*-

""" OpenERP core library."""

#----------------------------------------------------------
# Running mode flags (gevent, prefork)
#----------------------------------------------------------
# Is the server running with gevent.
import sys
evented = False
if sys.modules.get("gevent") is not None:
    evented = True

# Is the server running in pefork mode (e.g. behind Gunicorn).
# If this is True, the processes have to communicate some events,
# e.g. database update or cache invalidation. Each process has also
# its own copy of the data structure and we don't need to care about
# locks between threads.
multi_process = False

#----------------------------------------------------------
# libc UTC hack
#----------------------------------------------------------
# Make sure the OpenERP server runs in UTC. This is especially necessary
# under Windows as under Linux it seems the real import of time is
# sufficiently deferred so that setting the TZ environment variable
# in openerp.cli.server was working.
import os
os.environ['TZ'] = 'UTC' # Set the timezone...
import time              # ... *then* import time.
del os
del time

#----------------------------------------------------------
# Shortcuts
#----------------------------------------------------------
# The hard-coded super-user id (a.k.a. administrator, or root user).
SUPERUSER_ID = 1

def registry(database_name):
    """
    Return the model registry for the given database. If the registry does not
    exist yet, it is created on the fly.
    """
    return modules.registry.RegistryManager.get(database_name)

#----------------------------------------------------------
# Imports
#----------------------------------------------------------
import addons
import conf
import loglevels
import modules
import netsvc
import osv
import pooler
import release
import report
import service
import sql_db
import tools
import workflow

#----------------------------------------------------------
# Model classes, fields, api decorators, and translations
#----------------------------------------------------------
from . import models
from . import fields
from . import api
from openerp.tools.translate import _

#----------------------------------------------------------
# Other imports, which may require stuff from above
#----------------------------------------------------------
import cli
import http

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
