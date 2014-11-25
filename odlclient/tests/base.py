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

import os
import unittest
import odlclient as odl

SDNCTL = os.getenv("SDNCTL")
USER = os.getenv("SDNUSER")
PASS = os.getenv("SDNPASS")

class ApiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        auth = odl.Auth(server=SDNCTL, user=USER, password=PASS)
        cls.api = odl.Api(controller=SDNCTL, auth=auth)

    @classmethod
    def tearDownClass(cls):
        cls.api = None
