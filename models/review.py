#!/usr/bin/python3
""" module for Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """initialistion of Review that inherits from BaseModel class"""
    place_id = ""
    user_id = ""
    text = ""
