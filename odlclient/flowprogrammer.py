#!/usr/bin/env python
#
#   Copyright 2014 Hewlett-Packard Development Company, L.P.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import json
# Python3 compatibility
try:
    import urllib.parse as urllib
except ImportError:
    import urllib

from odlclient.api import ApiBase
import odlclient.datatypes as datatypes
from odlclient.error import raise_errors, DatatypeError


class FPin(ApiBase):
    """OpenFlow REST API Methods

    This class contains methods that call the OpenFlow
    REST API on the ODL SDN Controller

    - Topology Service
    - Node Service
    - Link Service
    - Path Planner
    - Path Diagnostics Service

    """
    def __init__(self, controller, restclient):
        super(FPin, self).__init__(controller, restclient)
        self._of_base_url = ("https://{0}:8443".format(self.controller) +
                             "/controller/nb/v2/flowprogrammer")



    def _assemble_flows(self, flows):
        if isinstance(flows, list):
            tmp = []
            for f in flows:
                if isinstance(f, datatypes.Flow):
                    tmp.append(f.to_dict())
                else:
                    raise DatatypeError(datatypes.Flow, f.__class__())
            data = {"flows": tmp}
        elif isinstance(flows, datatypes.Flow):
            data = {"flow": flows.to_dict()}
        else:
            raise DatatypeError([datatypes.Flow, list], f.__class__())
        return data

    def add_flows(self, dpid, flows, container=None):
        """Add a flow, or flows to the selected DPID

        :param str dpid: The datapath ID
        :param list, odlclient.datatypes.Flow flows: The flow or flows to add
        :param str container: container name

        """
        if container == None:
            container = "default"
        url = (self._of_base_url + '/' + container +
               'node/OF/{0}/staticFlow/flow1'.format(urllib.quote(dpid)))
        data = self._assemble_flows(flows)
        r = self.restclient.post(url, json.dumps(data))
        raise_errors(r)

    def update_flows(self, dpid, flows, container=None, flow_name=None):
        """Update a flow, or flows at the selected DPID

        :param str dpid: The datapath ID
        :param list, odlclient.datatypes.Flow flows:
            The flow or flows to update
        :param str container: container name
        :param str flow_name: flow name

        """
        if container == None:
            container = "default"
        if flow_name == None:
            flow_name = "flow1"
        url = (self._of_base_url + container +
               'node/OF/{0}/staticFlow/'.format(urllib.quote(dpid)) + flow_name)
        data = self._assemble_flows(flows)
        r = self.restclient.put(url, json.dumps(data))
        raise_errors(r)

    def delete_flows(self, dpid, flows, container=None, flow_name=None):
        """ Delete flow, or flows from the specified DPID

        :param str dpid: The datapath ID
        :param list, odlclient.datatypes.Flow flows:
            The flow or flows to delete
        :param str container: container name
        :param str flow_name: flow name
        """
        if container == None:
            container = "default"
        if flow_name == None:
            flow_name = "flow1"
        url = (self._of_base_url + container +
               'node/OF/{0}/staticFlow/'.format(urllib.quote(dpid)) + flow_name)
        data = self._assemble_flows(flows)
        r = self.restclient.delete(url, json.dumps(data))
        raise_errors(r)

    def get_groups(self, dpid):
        """Get a list of groups created on the DPID

        :param str dpid: The datapath ID
        :return: List of groups
        :rtype: list

        """
        url = (self._of_base_url +
               'datapaths/{0}/groups'.format(urllib.quote(dpid)))

        return self.restclient.get(url)

    def get_container(self, container):
        """Create a group

        :param str container: Container name

        """
        url = (self._of_base_url + urllib.quote(container))
        r = self.restclient.post(url, json.dumps(data))
        raise_errors(r)

