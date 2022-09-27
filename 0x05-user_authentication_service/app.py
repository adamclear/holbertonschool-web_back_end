#!/usr/bin/env python3
''' Flask App '''
from auth import Auth
from flask import abort, Flask, jsonify, redirect, request


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    ''' Returns a JSON payload '''
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    ''' Registers a new User '''
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    ''' Creates a new session for the user '''
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        return abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    ''' Logs the user out and destroys session '''
    try:
        AUTH.destroy_session(request.cookies['session_id'])
        return redirect('/')
    except Exception:
        abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    ''' Finds user by session id '''
    try:
        user = AUTH.get_user_from_session_id(request.cookies['session_id'])
        return jsonify({"email": user.email}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    ''' Creates a reset password token '''
    email = request.form.get('email')
    try:
        return jsonify({"email": email,
                        "reset_token": AUTH.get_reset_password_token(
                            email)}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
