#!/usr/bin/env python3
''' Basic Authentication class '''
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    ''' Basic Authentication class '''
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        ''' Returns Base64 part of Authorization header '''
        if authorization_header is None or type(authorization_header) != str\
                or not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        ''' Returns the decoded value of a Base64 string '''
        if base64_authorization_header is None\
                or type(base64_authorization_header) != str:
            return None
        try:
            decode_base = b64decode(base64_authorization_header)
            return decode_base.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' Returns the user email and password from the
        Base64 decoded value '''
        if decoded_base64_authorization_header is None or\
                type(decoded_base64_authorization_header) != str or\
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        return (decoded_base64_authorization_header.split(':')[0],
                decoded_base64_authorization_header.split(':')[1])
