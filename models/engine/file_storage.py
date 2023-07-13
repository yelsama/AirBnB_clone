#!/usr/bin/python3
''' FileStorage module '''
import json
from models.base_model import BaseModel
import models

class FileStorage:
    """filestorage"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in objects with keys"""
        self.__objects["{}.{}".format(obj.__class.__name__, obj.id)] = obj

    def save(self):
        """searilizes objects to json file"""
        new_dict = {}
        with open(self.__file_path, mode='w+', encoding='utf-8') as f:
            for m, k in self.__objects.items():
                new_dict[m] = k.to_dict()
                json.dump(new_dict, f)

    def reload(self):
        """deseralize the json file"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                newdata = json.loads(f)
                for m, k in newdata.items():
                    reloadedobj = eval('{}(**k)'.format(k['__class__']))
                    self.__objects[m] = reloadedobj

        except IOError:
            pass
