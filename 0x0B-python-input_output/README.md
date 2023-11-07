# Project: 0x0B. Python - Input/Output

## Description

This project focuses on input and output operations in Python. It covers topics like reading and writing files, JSON serialization and deserialization, and more.

## Learning Objectives

At the end of this project, you are expected to be able to explain:

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What the 'with' statement is and how to use it
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Tasks

1. **Read file**
   - Write a function that reads a text file (UTF8) and prints it to stdout.

2. **Write to a file**
   - Write a function that writes a string to a text file (UTF8) and returns the number of characters written.

3. **Append to a file**
   - Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.

4. **To JSON string**
   - Write a function that returns the JSON representation of an object (string).

5. **From JSON string to Object**
   - Write a function that returns an object (Python data structure) represented by a JSON string.

6. **Save Object to a file**
   - Write a function that writes an Object to a text file, using a JSON representation.

7. **Create object from a JSON file**
   - Write a function that creates an Object from a JSON file.

8. **Class to JSON**
   - Write a function that returns the dictionary description with simple data structure for JSON serialization of an object.

9. **Student to JSON**
   - Create a class `Student` with attributes `first_name`, `last_name`, and `age`, and a method `to_json` to retrieve a dictionary representation of the instance.

10. **Student to JSON with filter**
    - Enhance the `Student` class with a method `to_json` that allows filtering attributes to be retrieved.

11. **Student to disk and reload**
    - Modify the `Student` class to have methods `to_json` and `reload_from_json` to save and load instances from JSON.

12. **Pascal's Triangle**
    - Create a function that generates Pascal's Triangle up to a given number of rows.

13. **Search and update**
    - Create a function that inserts a line of text to a file after each line containing a specific string.

14. **Log parsing**
    - Write a script to read logs line by line and compute metrics, such as total file size and the number of lines by status code.

## Requirements

- Python scripts should be written and tested in Python 3.8.5
- Scripts should use the pycodestyle style guide
- All Python files should end with a newline
- All your files must be executable
- You can only use allowed editors (vi, vim, emacs)
