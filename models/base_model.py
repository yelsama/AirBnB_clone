#!/usr/bin/enb python3
"""
    class BaseModel that defines all common attributes/methods
    for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        initiate class arguments
        """
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    val = self.__class__.__name__
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """this makes modified copy of the dictionary"""
        a_dic = self.__dict__.copy()
        a_dic["created_at"] = self.created_at.isoformat()
        a_dic["updated_at"] = self.updated_at.isoformat()
        a_dic["__class__"] = self.__class__.__name__
        return a_dic

    def __str__(self):
        """set the print of instance"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id, self.__dict__)
