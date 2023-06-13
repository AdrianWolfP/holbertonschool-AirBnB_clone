#!/usr/bin/python3
"""Module for FileStorage class"""

import json
import models
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """class FileStorage serializes instances to
    a JSON file and deserializes JSON file to instances:
    private class attributes:
    __file_path: (string) - path to JSON file
    __objects: (dictionary) - empty nut will store all objects by <class name>.id"""
    
    __file_path = "./file.json"
    __objects = {}

    @classmethod
    def clear(cls):
        FileStorage.__objects = {}

    def all(self):
        """ returns dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """ set in __objects the obj with key <obj class name>.id """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)
    
    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key in data:
                    class_name = data[key]['__class__']
                    obj_dict = data[key]
                    cls = detattr(model, class_name)
                    instance = cls(**obj_dict)
                    self.__objects[key] = instance
        except FileNotFoundError:
            pass