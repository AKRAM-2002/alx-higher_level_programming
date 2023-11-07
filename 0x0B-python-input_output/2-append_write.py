#!/usr/bin/python3

"""append a text to a file"""
def append_write(filename="", text=""):
    """
         a function that appends a string at the end of a text file

         Args:
            filename (str): The name of the file to append to.
            text (str): The string to append to the file.
        Returns:
            The number of characters appended.
    """

    with open(filename,"a",encoding="utf-8") as f:
        return f.write(text)
