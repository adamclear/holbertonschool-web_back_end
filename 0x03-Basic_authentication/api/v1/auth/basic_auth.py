#!/usr/bin/env python3
''' Basic Authentication class '''
from api.v1.auth.auth import Auth, TypeVar
from base64 import b64decode
from models.user import User


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

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        ''' Returns User instance based on email and pwd '''
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        try:
            curUser = User.search({'email': user_email})
            for user in curUser:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        ''' Retrieves the User instance for a request '''
        try:
            getHeader = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(getHeader)
            decodeHeader = self.decode_base64_authorization_header(base64Header)
            userCredentials = self.extract_user_credentials(decodeHeader)
            return self.user_object_from_credentials(userCredentials[0],
                                                     userCredentials[1])
        except Exception:
            return None
