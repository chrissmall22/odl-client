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
import datetime

import requests


class Auth(requests.auth.AuthBase):
    """This class handles authentication against the ODL SDN REST API and
    uses the Requests API. Authderives from
    requests.auth.AuthBase and odlclient.ApiBase."""

    def __init__(self, server, user, password):
        """Initializes the class. Set the server, user and password
        member variables. Sets the token and expiration values to
        None"""
        super(Auth, self).__init__()
        self.server = server
        self.user = user
        self.password = password


    def __call__(self, request):
        """This method is called when an authentication token is
        required. We first check that the token exists and has not
        expired and then return the X-Auth-Token request header."""
        if (self.token is None or
                self.token_expiration <= datetime.datetime.now()):
            self.get_auth()
        request.headers['X-Auth-Token'] = self.token
        return request

    def get_auth(self):
        """This method requests an authentication token from the SDN
        controller and returns a dictionary with the token and
        expiration time."""
        auth = request.HTTPBasicAuth(self.user,self.passeord)
        return auth

    def delete_auth(self):
        """Delete Authentication Token, AKA, Logout. This method logs
        the current user out"""
