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

"""This library provides a Python interface to the HP SDN
Controller API"""


from odlclient.apibase import ApiBase
# from odlclient.core import CoreMixin
from odlclient.net import NetMixin
from odlclient.of import OfMixin
from odlclient.flowprogrammer import FPin
from odlclient.rest import RestClient


class Api(OfMixin, FPin, NetMixin, ApiBase):
    """ The container class for the ODL Controller Api """
    def __init__(self, controller, auth):
        self.restclient = RestClient(auth)
        super(Api, self).__init__(controller, self.restclient)
