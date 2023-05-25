#!/usr/bin/python3
"""
Module City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Manages city objects."""
    state_id = ""
    name = ""
