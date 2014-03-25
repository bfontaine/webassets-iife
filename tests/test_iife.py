# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

if platform.python_version() < '3.0':
    from StringIO import StringIO
else:
    from io import StringIO

import webassets_iife
from webassets_iife import IIFE

class TestIIFEFilter(unittest.TestCase):

    def setUp(self):
        self.iife = IIFE()

    # == version == #
    def test_version(self):
        self.assertRegexpMatches(webassets_iife.__version__, r'^\d+\.\d+\.\d+$')

    # == IIFE#output == #

    def test_iife_output(self):
        inp = 'xz32$1'
        out = StringIO()
        self.iife.output(StringIO(inp), out)
        out.seek(0)
        self.assertEquals(out.read(), ';!function(){%s}();' % inp)
