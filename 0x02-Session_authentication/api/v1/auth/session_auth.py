#!/usr/bin/env python3
"""
Create SessionAuth that inherits form Auth
"""
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Session authentication class"""
    pass
