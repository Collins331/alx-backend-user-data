#!/usr/bin/env python3
"""
Create SessionAuth that inherits form Auth
"""
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """ Session authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create session for user id"""
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        
        id = str(uuid4())
        self.user_id_by_session_id[id] = user_id

        return id
