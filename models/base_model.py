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
        a_dic = self.__dict__.copy()
        a_dic["created_at"] = self.created_at.isoformat()
        a_dic["updated_at"] = self.updated_at.isoformat()
        a_dic["__class__"] = self.__class__.__name__
        return a_dic

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__)
