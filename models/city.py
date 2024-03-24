#!/usr/bin/python3
"""City class module"""
from models.base_model import BaseModel


class City(BaseModel):
    """City management class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes city attributes"""
        super().__init__(*args, **kwargs)
