# -*- coding: utf-8 -*-

import types

def post_mortem(config, info):
    if config['debug_mode'] and isinstance(info[2], types.TracebackType):
        import pdb
        pdb.post_mortem(info[2])
