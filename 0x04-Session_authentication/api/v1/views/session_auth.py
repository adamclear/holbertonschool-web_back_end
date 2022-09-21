#!/usr/bin/env python3
''' SessionAuth views '''
from api.v1.views import app_views
from api.v1.auth.session_auth import SessionAuth
from flask import abort, jsonify, make_response, request
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    ''' Logs user in '''
    email = request.form.get('email')
    if email is None:
        return (jsonify({'error': 'email missing'}), 400)
    passwd = request.form.get('password')
    if passwd is None:
        return (jsonify({'error': 'password missing'}), 400)
    user_list = User.search({'email': email})
    if len(user_list) == 0:
        return (jsonify({'error': 'no user found for this email'}), 404)
    for user in user_list:
        if not user.is_valid_password(passwd):
            return (jsonify({'error': 'wrong password'}), 401)
        else:
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            response = jsonify(user.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return (response)
