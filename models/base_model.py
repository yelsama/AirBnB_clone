#!/usr/bin/enb python3
"""
    class BaseModel that defines all common attributes/methods
    for other classes
"""
import uuid
from datetime import datetime

class BaseModel:
    """for common attributes"""
    def __init__(self):
        self.my_number = 0
        self.name = ''
        self.id = str(uuid.uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__.update({'__class__': self.__class__.__name__})
        # self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__)
