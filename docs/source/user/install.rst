.. _install:

Installation
============

This part of the documentation covers the installation of the ODL SDN Client.
The first step to using any software package is getting it properly installed.

Distribute & Pip
----------------

Installing the ODL SDN Client is simple with `pip <http://www.pip-installer.org/>`_::

    $ pip install odl-client

or, with `easy_install <http://pypi.python.org/pypi/setuptools>`_::

    $ easy_install odl-client

Get the Code
------------

The ODL Client is actively developed on GitHub, where the code is
`always available <https://github.com/chrissmall22/odl-client>`_.

You can either clone the public repository::

    git clone git://github.com/chrissmall22/odl-client.git

Download the `tarball <https://github.com/chrissmall22/odl-client/tarball/master>`_::

    $ curl -OL https://github.com/chrissmall22/odl-client/tarball/master

Or, download the `zipball <https://github.com/chrissmall22/odl-client/zipball/master>`_::

    $ curl -OL https://github.com/chrissmall22/odl-client/zipball/master

Once you have a copy of the source, you can embed it in your Python package,
or install it into your site-packages easily::

    $ python setup.py install