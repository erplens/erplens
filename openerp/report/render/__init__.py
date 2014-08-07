# -*- coding: utf-8 -*-

from simple import simple
from rml import rml, rml2html, rml2txt, odt2odt , html2html, makohtml2html
from render import render


try:
    from PIL import Image
except ImportError:
    import logging
    _logger = logging.getLogger(__name__)
    _logger.warning('Python Imaging not installed, you can use only .JPG pictures !')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

