#!/usr/bin/env python3
''' Basic Authentication class '''
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    ''' Basic Authentication class '''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        ''' Returns Base64 part of Authorization header '''
        if authorization_header is None or type(authorization_header) != str\
                or not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(' ')[1]
