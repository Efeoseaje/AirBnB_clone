#!/usr/bin/python3
import json
from models.base_model import BaseModel
"""file_storage.py module"""


class FileStorage():
    """
    Function: It serialize instance to JSON file and
    deserialize JSON file to instance

    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """
        Function: Return the Dictionary 
        Return: __objects

        """

        return FileStorage.__objects
    
    def new(self, obj):

        key = self.__class__.__name__ + "." + self.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Function: serializes _objects to the JSON file
        """
        with open(__file_path, "w") as json_file:
            json.dump(__object, json_file)

    def reload(self):
        """
        Function: Deserialize the JSON file if it exist,
        otherwise it does nothing.

        """
        try:
            with open(__file_path, "r") as json_file:
                object = json.load(json_file)
        except FileNotFoundError:
            pass
