#!/usr/bin/python3
"""user class
"""

from models.base_model import BaseModel


class User(BaseModel):
    '''Manages User objects'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
