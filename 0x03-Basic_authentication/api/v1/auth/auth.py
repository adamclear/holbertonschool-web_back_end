#!/usr/bin/env python3
''' API authentication class '''
from flask import request
from typing import List, TypeVar


class Auth():
    ''' API authentication class '''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        ''' Currently just returns False '''
        return False


    def authorization_header(self, request=None) -> str:
        ''' Currently just returns None '''
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        ''' Currently just returns None '''
        return None
