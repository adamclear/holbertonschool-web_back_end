#!/usr/bin/env python3
''' This module contains the function to encrypt and validate passwords '''
import bcrypt


def hash_password(password: str) -> bytes:
    ''' Hashes a password using bcrypt. '''
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    ''' Validates password against hashed password. '''
    return bcrypt.checkpw(password.encode(), hashed_password)
