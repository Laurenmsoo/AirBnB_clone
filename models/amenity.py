#!/usr/bin/python
"""Amenity class module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes amenity class attributes"""
        super().__init__(*args, **kwargs)
