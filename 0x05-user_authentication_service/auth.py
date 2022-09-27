#!/usr/bin/env python3
''' Auth functions '''
import bcrypt


def _hash_password(password: str) -> str:
    ''' Hashes a password using bcrypt '''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
