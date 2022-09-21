#!/usr/bin/env python3
''' SessionAuth class '''
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    ''' SessionAuth class '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' Creates a session ID for a user_id '''
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id.update({session_id: user_id})
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        ''' Returns a user ID based on a session ID '''
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        ''' Returns a User instance based on cookie value '''
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)
