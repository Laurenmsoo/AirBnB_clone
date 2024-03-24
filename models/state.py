#!/usr/bin/python3
"""State class module"""
from models.base_model import BaseModel


class State(BaseModel):
    """Stste class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes the state class attributes"""
        super().__init__(*args, **kwargs)
