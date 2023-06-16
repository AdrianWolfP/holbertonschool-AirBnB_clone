#!/usr/bin/python3
"""Module for FileStorage class"""

import json
import models
import os
from typing import Dict


class FileStorage:
    """
    Class FileStorage 
    serializes instances to a JSON file 
    and deserializes JSON file to instances
    """

    def __init__(self):
        self.file_path = "./file.json"
        self.objects = {}

    def clear(self):
        """
        Clears the objects dictionary
        """
        self.objects = {}

    def all(self) -> Dict[str, object]:
        """
        Returns the objects dictionary
        """
        return self.objects
    
    def new(self, obj: object):
        """
        Adds an object to the objects dictionary
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.objects[key] = obj

    def save(self):
        """
        Serializes the objects
        to the JSON file
        """
        new_dict = {key: value.to_dict() for key, value in self.objects.items()}
        with open(self.file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        reload_dict = {"BaseModel": BaseModel, "User": User, "State": State,
                       "City": City, "Amenity": Amenity, "Place": Place,
                       "Review": Review}

        if os.path.isfile(self.file_path):
            with open(self.file_path, "r", encoding="UTF-8") as f:
                reloaded = json.load(f)
                for obj, value in reloaded.items():
                    item_class = reloaded[obj].get("__class__")
                    if item_class in reload_dict:
                        cls_func = reload_dict.get(item_class)
                        self.objects[obj] = cls_func(**reloaded[obj])
