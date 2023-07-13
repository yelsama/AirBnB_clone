#!/usr/bin/enb python3
"""
    class BaseModel that defines all common attributes/methods
    for other classes
"""
import uuid
from datetime import datetime
import models

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
        models.storage.save()

    def to_dict(self):
        """this makes modified copy of the dictionary"""
        a_dic = self.__dict__.copy()
        a_dic["created_at"] = self.created_at.isoformat()
        a_dic["updated_at"] = self.updated_at.isoformat()
        a_dic["__class__"] = self.__class__.__name__
        return a_dic

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                    self.id, self.__dict__)

    def __int__(self, *args, **kwargs):
        """initialise a basemodel"""

        if len(kwargs) != 0:
            self.__dict__ = kwargs
            self.created_at = datetime.strptime(self.created_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(self.updated_at,
                                                "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            model.storage.new(self)
