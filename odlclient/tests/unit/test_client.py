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

import unittest

from odlclient.api import Api
from odlclient.auth import Auth
from odlclient.apibase import ApiBase
#from odlclient.core import CoreMixin
from odlclient.net import NetMixin
from odlclient.of import OfMixin


class ApiTestCase(unittest.TestCase):
    def setUp(self):
        self.auth = Auth(server='example.com',
                               user='sdn',
                               password='skyline'
        )

    def test_api_instantiation(self):
        api = Api('10.10.10.10', self.auth)
        self.assertTrue(isinstance(api, ApiBase))
        #self.assertTrue(isinstance(api, CoreMixin))
        self.assertTrue(isinstance(api, NetMixin))
        self.assertTrue(isinstance(api, OfMixin))
        self.assertEqual(api.restclient.auth, self.auth)
        self.assertEqual(api.controller, '10.10.10.10')
