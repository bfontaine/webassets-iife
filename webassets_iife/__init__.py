# -*- coding: UTF-8 -*-


"""
IIFE filter for webassets. It wraps a JS bundle in an IIFE, thus preventing
global leaks.
"""

from webassets.filter import Filter, register_filter

__version__ = '0.1.0'
__all__ = ('IIFE',)


class IIFE(Filter):
    name = 'iife'
    max_debug_level = None

    def output(self, _in, out, **kw):
        out.write(';!function(){')
        out.write(_in.read())
        out.write('}();')

register_filter(IIFE)
