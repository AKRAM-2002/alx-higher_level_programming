#!/usr/bin/python3
"""Read_file function"""
def read_file(filename=""):
    """A function that reads a text file"""

    with open(filename,'r',encoding='utf-8') as f:
        print(f.read(), end="")
