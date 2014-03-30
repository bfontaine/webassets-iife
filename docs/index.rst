.. webassets-iife documentation master file, created by
   sphinx-quickstart on Sun Mar 30 16:52:03 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to webassets-iife's documentation!
==========================================

.. toctree::
   :maxdepth: 2

``webassets-iife`` is a webassets_ filter to wrap a JavaScript bundle in an
IIFE to prevent global leaks and improve minification.

.. _webassets: https://webassets.readthedocs.org/en/latest/

Installation
------------

Install ``webassets-iife`` with ``pip``: ::

    [sudo] pip install webassets-iife

It supports both Python 2.x and 3.x.

Usage
-----

With Flask
~~~~~~~~~~

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
