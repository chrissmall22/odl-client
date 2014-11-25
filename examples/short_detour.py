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

import odlclient as odl

def main():
    #initialize the api
    controller = '15.126.229.78'
    auth = hp.Auth(user="sdn", pass="skyline", controller="127.0.0.1")
    api = odl.Api(controller=controller, auth=auth)

    #create the match object
    match = odl.datatypes.Match(eth_type="ipv4", ipv4_src="10.0.0.1",
                               ipv4_dst="10.0.0.22",ip_proto="tcp",
                               tcp_dst="80")

    #create the action objects
    output1 = odl.datatypes.Instruction(output=1)
    output6 = odl.datatypes.Instruction(output=6)

    #create the flows
    flow1 = odl.datatypes.Flow(priority=30000, idle_timeout=30,
                              match=match, instruction=output6)
    flow2 = odl.datatypes.Flow(priority=30000, idle_timeout=30,
                              match=match, instruction=output1)

    #push the flows to the datatpaths
    api.add_flows('00:00:00:00:00:00:00:01', flow1)
    api.add_flows('00:00:00:00:00:00:00:02', flow1)
    api.add_flows('00:00:00:00:00:00:00:03', flow2)

if __name__ == "__main__":
    main()
