#!/usr/bin/python3
"""Defines a class Student."""
class Student:

    """ Class Student"""
    def __init__(self, first_name, last_name, age):
        '''
         A constructor for class student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs = None):
        """Get a dictionary representation of the Student."""
        if (type(attrs) == list and all(type(subAttr) == str for subAttr in attrs)):
            return {k: getattr(self,k) for k in attrs if hasattr(self,k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reload object attributes from a dictionary."""
        for key, value in json.items():
            setattr(self,key,value)
