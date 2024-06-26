#!/usr/bin/python3
"""This module creates a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialiazes user class attributes"""
        super().__init__(*args, **kwargs)
