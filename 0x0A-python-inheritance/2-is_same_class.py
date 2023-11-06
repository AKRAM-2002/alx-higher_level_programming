#!/usr/bin/python3
""" Exact same object """
def is_same_class(obj, a_class):
    '''
       Returns true or false to see if the object is exactly an instance of the class

    '''
    if isinstance(obj,a_class):
        return True
    return False
