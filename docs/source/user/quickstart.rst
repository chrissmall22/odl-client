.. _quickstart:

Quickstart
==========

.. module:: odlclient.api

Eager to get started? This page gives a good introduction in how to get started
with the ODL SDN Client. If you haven't installed it already,
head over to the :ref:`Installation <install>` section.

Using the API
--------------

Using the ODL SDN Client to interface with the ODL Controller REST API is simple.

First we import the HP SDN Client module using the short name ``hp`` ::

    >>> import odlclient as odl

Then, we create an Auth authenticator::

    >>> auth = hp.Auth(user="odl", pass="odl", controller="127.0.0.1")

This creates a :class:`Auth` authenticator called ``auth`` which is required to instantiate the :class:`Api` object::

    >>> api = hp.Api(controller='10.10.10.10', auth=auth)

Now, we have a :class:`Api` object called ``api``. This object allows us to access the ODL SDN Controller API using simple method calls.
For example::

    >>> api.get_datapaths()

Which will return a list of all Datapaths discovered by the HP VAN SDN Controller.

Full documentation for each of the methods is available in the :ref:`Core REST API <core>`,
:ref:`OpenFlow REST API <of>` and :ref:`Network Services REST API <net>` sections.

Errors and Exceptions
---------------------

If things go wrong, the ODL SDN Client will raise exceptions for your application to handle.
The following exceptions are raised based on the error message give to us by the ODL SDN Controller.

A :class:`~odlclient.error.InvalidJson` exception is raised when the JSON submitted in a POST request is invalid

A :class:`~odlclient.error.VersionMismatch` exception is raised when a Datapath does not support the requisite OpenFlow version for a specific feature

A :class:`~odlclient.error.IllegalArgument` exception is raised when an illegal argument is passed to the SDN Controller API

A :class:`~odlclient.error.OpenflowProtocolError` exception is raised when the something goes wrong at the OpenFlow layer

A :class:`~odlclient.error.NotFound` exception is raised when the requested resource is not found

If something goes wrong in the conversion between JSON and Python Objects, a
:class:`odlclient.error.DatatypeError` exception is raised

All exceptions that the HP SDN Client explicitly raises inherit from
:class:`odlclient.error.OdlclientError`.

In the event of an error at the HTTP layer that can't be handled, we allow the Requests library to raise an exception.
