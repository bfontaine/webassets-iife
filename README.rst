==============
webassets-iife
==============

.. image:: https://img.shields.io/travis/bfontaine/webassets-iife.png
   :target: https://travis-ci.org/bfontaine/webassets-iife
   :alt: Build status

.. image:: https://img.shields.io/coveralls/bfontaine/webassets-iife/master.png
   :target: https://coveralls.io/r/bfontaine/webassets-iife?branch=master
   :alt: Coverage status

.. image:: https://img.shields.io/pypi/v/webassets-iife.png
   :target: https://pypi.python.org/pypi/webassets-iife
   :alt: Pypi package

.. image:: https://img.shields.io/pypi/dm/webassets-iife.png
   :target: https://pypi.python.org/pypi/webassets-iife

``webassets-iife`` is a webassets_ filter to wrap a JavaScript bundle in an
IIFE to prevent global leaks and improve minification.

.. _webassets: https://webassets.readthedocs.org/en/latest/

Install
-------

.. code-block::

    pip install webassets-iife

The filter works with both Python 2.x and 3.x.

Usage
-----

For example with Flask:

.. code-block::

    from flask.ext.assets import Environment, Bundle
    from webassets_iife import IIFE

    # ...

    assets = Environment(app)

    js = Bundle('myscript1.js',
                'myscript2.js',
                filters=(IIFE, 'closure_js'), output='all.min.js')
    assets.register('js_all', js)

This will concat ``myscript1.js`` and ``myscript2.js`` into one JS chunk, wrap
it in an IIFE and minify it.

IIFE?
-----

An *IIFE* is an Immediately-Invoked Function Expression. It’s an anonymous
function that’s declared and invoked immediately after that. It’s used in
JavaScript to create a closed environment which can’t be accessed from the
outside.

.. code-block::

    // a and b can be accessed by external code
    var a = 3,
        b = 1;
    // ... some code ...

    // a and b can't be accessed by external code
    (function() {
        var a = 3,
            b = 1;
        // ... some code ...
    })();

Wrapping code in an IIFE helps the minifier see the dead code, because it
*knows* that these local variables can’t be accessed from the outside and thus
can remove them or mangled their name.
