#!/usr/bin/python3
"""Definition of the Base class"""

import json
import csv
import os


class Base:
    """A class representing the Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the Base instance"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if (type(list_dictionaries) != list or
                not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of objects to a file in CSV format"""
        if (type(list_objs) != list and
                list_objs is not None or
                not all(isinstance(x, cls) for x in list_objs)):
            raise TypeError("list_objs must be a list of instances")

        filename = cls.__name__ + ".csv"
        with open(filename, 'w') as f:
            if list_objs is not None:
                list_objs = [x.to_dictionary() for x in list_objs]
                if cls.__name__ == 'Rectangle':
                    fields = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == 'Square':
                    fields = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @staticmethod
    def from_json_string(json_string):
        """Return a list of objects from a JSON string"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance of the Base class"""
        if cls.__name__ == 'Rectangle':
            new_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Load a list of objects from a file in JSON format"""
        filename = cls.__name__ + ".json"
        loaded_objects = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                json_string = f.read()
                list_dicts = cls.from_json_string(json_string)
                for d in list_dicts:
                    loaded_objects.append(cls.create(**d))
        return loaded_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None or list_objs == []:
            jstr = "[]"
        else:
            jstr = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """Return the list from the JSON string representation json_string."""
        new_list = []
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
            new_list = json.loads(json_string)
        return new_list

