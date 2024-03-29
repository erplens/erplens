# -*- coding: utf-8 -*-

""" OpenERP core exceptions.

This module defines a few exception types. Those types are understood by the
RPC layer. Any other exception type bubbling until the RPC layer will be
treated as a 'Server error'.

If you consider introducing new exceptions, check out the test_exceptions addon.
"""

# kept for backward compatibility
class except_orm(Exception):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.args = (name, value)

class Warning(Exception):
    pass

class RedirectWarning(Exception):
    """ Warning with a possibility to redirect the user instead of simply
    diplaying the warning message.

    Should receive as parameters:
      :param int action_id: id of the action where to perform the redirection
      :param string button_text: text to put on the button that will trigger
          the redirection.
    """

class AccessDenied(Exception):
    """ Login/password error. No message, no traceback. """
    def __init__(self):
        super(AccessDenied, self).__init__('Access denied.')
        self.traceback = ('', '', '')

class AccessError(except_orm):
    """ Access rights error. """
    def __init__(self, msg):
        super(AccessError, self).__init__('AccessError', msg)

class MissingError(except_orm):
    """ Missing record(s). """
    def __init__(self, msg):
        super(MissingError, self).__init__('MissingError', msg)

class DeferredException(Exception):
    """ Exception object holding a traceback for asynchronous reporting.

    Some RPC calls (database creation and report generation) happen with
    an initial request followed by multiple, polling requests. This class
    is used to store the possible exception occuring in the thread serving
    the first request, and is then sent to a polling request.

    ('Traceback' is misleading, this is really a exc_info() triple.)
    """
    def __init__(self, msg, tb):
        self.message = msg
        self.traceback = tb

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
