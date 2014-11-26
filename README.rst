OpenDayLight SDN Client
=============
.. image:: https://travis-ci.org/chrissmall22/odl-client.png?branch=master
    :target: https://travis-ci.org/chrissmall22/odl-client
.. image:: https://img.shields.io/coveralls/chrissmall22/odl-client.svg
    :target: https://coveralls.io/r/chrissmall22/odl-client?branch=master
    
**A Python library that makes interaction with the OpenDayLight Controller REST API easy**

Author: Chris Small, Hewlett Packard

Based on the hp-sdn-client written by Dave Tucker, Hewlett Packard


Usage Example
-------------

To use the library::

    import odlclient as odl
    controller = '10.44.254.129'
    auth = odl.XAuthToken(user='odl', password='odl', server=controller)
    api = odl.Api(controller=controller, auth=auth)

    api.get_datapaths()


Sample Application
------------------

Please see examples/short_detour.py

Running the Tests
-----------------

The unit tests can be run with tox. Make sure you have modified odlclient/tests/tests.py before you run::

    tox -e py27 -v -- -v

tox.ini has py26, py27 and py33 environments, but only py27 is supported today.

For functional testing, a working ODN Controller is required. Mininet is used to generate a test topology.

Set your environment variables on your workstation and mininet VM as follows::

    export SDNCTL="10.44.254.129"
    export SDNUSER="odl"
    export SDNPASS="odl"

It is recommended to download the Mininet VM. On the VM, start the following topology::

    sudo mn --topo tree,2,6 --mac --switch ovsk --controller remote,ip=$SDNCTL

Run the functional tests using::

    tox -e functional

The functional test for applciation uploads requires access to the internet to donwload a sample appliction.

