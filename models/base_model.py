#!/usr/bin/enb python3
"""
    class BaseModel that defines all common attributes/methods
    for other classes
"""
import uuid
from datetime import datetime

class BaseModel:
    """for common attributes"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()
    def __init__(self):
        self.name = ''
        self.my_number = 0
