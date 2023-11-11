#!/usr/bin/python3
"""  Search and update """
def append_after(filename="", search_string="", new_string=""):

    """
    Append a string after the first occurrence of a specified search string in a file.

    Parameters:
    - filename (str): The name of the file to modify.
    - search_string (str): The string to search for in each line of the file.
    - new_string (str): The string to append after the first occurrence of the search string.

    Raises:
    - FileNotFoundError: If the specified file is not found.

    """


    try:
        with open(filename) as f:
            new_file = ""
            for line in f:
                new_file += line
                if search_string in line:
                    new_file += new_string

        with open(filename, "w") as w:
            w.write(new_file)

    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")


