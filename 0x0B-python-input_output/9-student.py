#!/usr/bin/python3

""" Student to JSON"""
class Student:

    """ Class Student"""
    def __init__(self, first_name, last_name, age):
        '''
         A constructor for class student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
