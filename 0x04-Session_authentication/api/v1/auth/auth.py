#!/usr/bin/env python3
''' API authentication class '''
from flask import request
from os import getenv
from typing import List, TypeVar


class Auth():
    ''' API authentication class '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' Defines which routes don't need authentication. '''
        if path is None or excluded_paths is None:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        ''' Validates requests to secure the API '''
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        ''' Currently just returns None '''
        return None

    def session_cookie(self, request=None):
        ''' Returns a cookie value from a request '''
        if request is None:
            return None
        cookie = getenv('SESSION_NAME')
        return request.cookies.get(cookie)
