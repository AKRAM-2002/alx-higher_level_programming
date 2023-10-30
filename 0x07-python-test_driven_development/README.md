# 0x07. Python - Test-driven development

**Project Description:**

0x07. Python - Test-driven development is a project aimed at reinforcing your Python programming skills by focusing on test-driven development (TDD). TDD is a software development approach that emphasizes writing tests before writing the actual code. In this project, you will work on a series of tasks to practice TDD and strengthen your Python programming knowledge.

## Table of Contents

- [Introduction](#introduction)
- [Project Details](#project-details)
- [Project Requirements](#project-requirements)
- [Project Tasks](#project-tasks)
  - [Task 0: Integers Addition](#task-0-integers-addition)
  - [Task 1: Divide a Matrix](#task-1-divide-a-matrix)
  - [Task 2: Say My Name](#task-2-say-my-name)
  - [Task 3: Print Square](#task-3-print-square)
  - [Task 4: Text Indentation](#task-4-text-indentation)
  - [Task 5: Max Integer - Unittest](#task-5-max-integer-unittest)
  - [Task 6: Matrix Multiplication](#task-6-matrix-multiplication)
  - [Task 7: Lazy Matrix Multiplication](#task-7-lazy-matrix-multiplication)
  - [Task 8: CPython #3: Python Strings](#task-8-cpython-3-python-strings)

## Introduction

Welcome to the project "0x07. Python - Test-driven development." This project is designed to help you improve your Python programming skills by focusing on test-driven development (TDD). TDD is a software development approach that emphasizes writing tests before writing the actual code. In this project, you will work on a series of tasks to practice TDD and strengthen your Python programming knowledge.

## Project Details

### Project Timeline

- Start Date: October 26, 2023, 4:00 AM
- End Date: November 1, 2023, 4:00 AM
- Checker Release Date: November 1, 2023, 4:00 AM

### Resources

Please read or watch the following resources:

- [doctest - Test interactive Python examples](https://docs.python.org/3/library/doctest.html) (until "26.2.3.7. Warnings" included)
- [doctest – Testing through documentation](https://docs.python.org/3/library/doctest.html)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)
- [Unittest module](https://docs.python.org/3/library/unittest.html)
- [Interactive and Non-interactive tests](https://docs.python.org/3/library/doctest.html)

### Learning Objectives

By the end of this project, you should be able to explain the following without the help of Google:

- General understanding of why Python programming is awesome.
- What is an interactive test and why tests are important.
- How to write docstrings to create tests.
- How to write documentation for each module and function.
- Knowledge of the basic option flags to create tests.
- How to find and handle edge cases.

### Copyright and Plagiarism

You are responsible for creating solutions for the tasks yourself in order to meet the learning objectives. Copying and pasting someone else's work is not allowed, and any form of plagiarism is strictly forbidden and will result in removal from the program.

## Project Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should follow the pycodestyle (version 2.8.*) guidelines.
- All your files must be executable.
- The length of your files will be tested using `wc`.

### Python Test Cases

- Allowed editors: vi, vim, emacs.
- All your test files should end with a new line.
- All your test files should be inside a folder named `tests`.
- All your test files should be text files with the extension `.txt`.
- All your tests should be executed by using the command: `python3 -m doctest ./tests/*`.
- All your modules should have documentation (use `python3 -c 'print(__import__("my_module").__doc__)'`).
- All your functions should have documentation (use `python3 -c 'print(__import__("my_module").my_function.__doc__)'`).
- Documentation should be a real sentence explaining the purpose of the module, class, or method (the length of it will be verified).
- Collaboration on test cases is encouraged to ensure all edge cases are covered, as the Checker checks for tests.

## Project Tasks

### Task 0: Integers Addition

**Description:** Write a function that adds two integers. The function should have the following prototype:

```python
def add_integer(a, b=98):
a and b must be integers or floats; otherwise, raise a TypeError exception with the message "a must be an integer" or "b must be an integer".
If a and b are floats, they should be cast to integers.
The function should return an integer, which is the addition of a and b.
You are not allowed to import any module.

**Example:**
print(add_integer(1, 2))  # Output: 3
print(add_integer(100, -2))  # Output: 98
print(add_integer(2))  # Output: 100
print(add_integer(100.3, -2))  # Output: 98
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)  # Output: b must be an integer
try:
    print(add_integer(None))
except Exception as e:
    print(e)  # Output: a must be an integer

Requirements:

Files: 0-add_integer.py, tests/0-add_integer.txt
Task 1: Divide a Matrix
Description: Write a function that divides all elements of a matrix. The function should have the following prototype:

def matrix_divided(matrix, div):

matrix must be a list of lists of integers or floats; otherwise, raise a TypeError exception with the message "matrix must be a matrix (list of lists) of integers/floats".
Each row of the matrix must be of the same size; otherwise, raise a TypeError exception with the message "each row of the matrix must have the same size".
div must be a number (integer or float); otherwise, raise a TypeError exception with the message "div must be a number".
div can't be equal to 0; otherwise, raise a ZeroDivisionError exception with the message "division by zero".
All elements of the matrix should be divided by div and rounded to 2 decimal places.
The function should return a new matrix.
You are not allowed to import any module.

**Example:**
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
# Output:
# [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

Requirements:

Files: 2-matrix_divided.py, tests/2-matrix_divided.txt
Task 2: Say My Name
Description: Write a function that prints "My name is <first name> <last name>." The function should have the following prototype:


def say_my_name(first_name, last_name=""):
first_name and last_name must be strings; otherwise, raise a TypeError exception with the message "first_name must be a string" or "last_name must be a string".
The function should print "My name is <first name> <last name>."
Example:


say_my_name("John", "Doe")
# Output: My name is John Doe
say_my_name("John")
# Output: My name is John
Requirements:

Files: 3-say_my_name.py, tests/3-say_my_name.txt
Task 3: Print Square
Description: Write a function that prints a square with the character #. The function should have the following prototype:


def print_square(size):
size is the size length of the square. size must be an integer greater than or equal to 0; otherwise, raise a TypeError exception with the message "size must be an integer" or "size must be >= 0".
The function should print the square using the # character.
You are not allowed to import any module.
Example:


print_square(4)
# Output:
# ####
# ####
# ####
# ####
Requirements:

Files: 4-print_square.py, tests/4-print_square.txt
Task 4: Text Indentation
Description: Write a function that prints text with two new lines after each of these characters: ., ?, and :. The function should have the following prototype:


def text_indentation(text):
text must be a string; otherwise, raise a TypeError exception with the message "text must be a string".
There should be no space at the beginning or end of each printed line.
You are not allowed to import any module.
Example:


text = "This is a simple text. But this text, is not so simple."
text_indentation(text)
# Output:
# This is a simple text.
# But this text, is not so simple.
Requirements:

Files: 5-text_indentation.py, tests/5-text_indentation.txt
Task 5: Max Integer - Unittest
Description: In this task, you will write test cases for the max_integer function from the 6-max_integer.py module. The max_integer function is intended to find and return the largest integer in a list of integers. You need to write test cases to ensure this function works correctly.

Your test cases should be in a file named 6-max_integer_test.py inside the tests folder.
The test cases should use the unittest module.
You should have test cases that cover different scenarios, such as:
A list with positive integers.
A list with negative integers.
A list with both positive and negative integers.
An empty list (where the function should return None).
A list that contains non-integer elements (where the function should raise a TypeError).
Your test cases should thoroughly check the behavior of the max_integer function.
Requirements:

Files: 6-max_integer.py, tests/6-max_integer_test.py
Task 6: Matrix Multiplication
Description: Write a function that multiplies 2 matrices. The function should have the following prototype:


def matrix_mul(m_a, m_b):
m_a and m_b must be lists of lists of integers or floats.
If m_a or m_b is not a list of lists, raise a TypeError exception with the message "m_a must be a list of lists" or "m_b must be a list of lists."
If m_a or m_b is an empty list, raise a ValueError exception with the message "m_a can't be empty" or "m_b can't be empty."
If m_a or m_b contain elements that are not integers or floats, raise a TypeError exception with the message "m_a should contain only integers or floats" or "m_b should contain only integers or floats."
If m_a and m_b have different lengths, raise a ValueError exception with the message "each row of m_a must be of the same size" or "each row of m_b must be of the same size."
If the number of columns in m_a is different from the number of rows in m_b, raise a ValueError exception with the message "m_a and m_b can't be multiplied."
You are not allowed to import any module.
Example:


m_a = [[1, 2], [3, 4]]
m_b = [[2, 0], [1, 2]]
print(matrix_mul(m_a, m_b))
# Output: [[4, 4], [10, 8]]
Requirements:

Files: 100-matrix_mul.py, tests/100-matrix_mul.txt
Task 7: Lazy Matrix Multiplication
Description: Write a function that multiplies 2 matrices by using the NumPy module. The function should have the following prototype:


def lazy_matrix_mul(m_a, m_b):
m_a and m_b must be lists of lists of integers or floats.
If m_a or m_b is not a list of lists, raise a TypeError exception with the message "m_a must be a list of lists" or "m_b must be a list of lists."
If m_a or `
