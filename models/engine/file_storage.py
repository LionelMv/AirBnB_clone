#!/usr/bin/python3
'''File Storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''serializes and deserialzes json files'''

    __file_path = 'file.json'
    __objects = {}
    class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                  "City": City, "Amenity": Amenity, "Place": Place,
                  "Review": Review}

    def all(self):
        '''Return dictionary of <class>.<id> : object instance'''
        return self.__objects

    def new(self, obj):
        '''Add new obj to existing dictionary of instances'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (__file_path)"""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dic = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dic, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                # key = BaseModel.id
                # e.g. obj = self.class_dict["BaseModel"](**value)
                # obj = self.class_dict[value['__class__']](**value)
                # self.__objects[key] = obj
                # self.new(obj)
                class_name = key.split(".")[0]
                obj = eval(class_name)(**value)
                self.new(obj)
        except FileNotFoundError:
            pass
