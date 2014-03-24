==============
webassets-iife
==============

.. image:: https://img.shields.io/pypi/v/webassets-iife.png
   :target: https://pypi.python.org/pypi/webassets-iife
   :alt: Pypi package

``webassets-iife`` is a webassets_ filter to wrap a JavaScript bundle in an
IIFE to prevent global leaks and improve minification.

.. _webassets: https://webassets.readthedocs.org/en/latest/

Install
-------

.. code-block::

    pip install webassets-iife

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

