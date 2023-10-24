# Python - Classes and Objects

## Table of Contents
1. [Background Context](#background-context)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Copyright and Plagiarism](#copyright-and-plagiarism)
5. [Requirements](#requirements)
6. [Tasks](#tasks)

## Background Context
Welcome to the "Python - Classes and Objects" project. In this project, you will explore the world of Object-Oriented Programming (OOP) in Python. OOP is a fundamental concept in programming, and this project will introduce you to the basics of classes, objects, attributes, methods, and more. It is essential that you read and understand the provided resources to successfully complete the tasks and meet the learning objectives.

## Resources
Before you dive into the tasks, make sure to read or watch the following resources in the specified order:

- [Object Oriented Programming](#) (Read everything until the paragraph "Inheritance" excluded. You do NOT have to learn about class attributes, classmethod, and staticmethod yet).
- [Object-Oriented Programming](#) (Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The __init__ Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”).
- [Properties vs. Getters and Setters](#)
- [Learn to Program 9: Object Oriented Programming](#)
- [Python Classes and Objects](#)
- [Object Oriented Programming](#)

## Learning Objectives
By the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General:**
- Understand why Python programming is awesome.
- Define what Object-Oriented Programming (OOP) is.
- Explain the concept of "first-class everything."
- Describe what a class is.
- Differentiate between a class and an object or instance.
- Define what an attribute is and how to use public, protected, and private attributes.
- Understand the concept of 'self' in Python.
- Define what a method is.
- Explain the purpose of the special `__init__` method and how to use it.
- Understand the concepts of Data Abstraction, Data Encapsulation, and Information Hiding.
- Define what a property is.
- Differentiate between an attribute and a property in Python.
- Describe the Pythonic way to write getters and setters.
- Learn how to dynamically create arbitrary new attributes for existing instances of a class.
- Understand how to bind attributes to objects and classes.
- Explain what the `__dict__` of a class and/or instance of a class is and what it contains.
- Understand how Python finds the attributes of an object or class.
- Learn how to use the `getattr` function.

**Copyright - Plagiarism:**
- Be aware of the strict prohibition of plagiarism.
- Avoid copying and pasting someone else's work.
- Do not publish any content of this project.

## Requirements
**General:**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)`)
- A documentation is not a simple word, it's a real sentence explaining the purpose of the module, class, or method (the length of it will be verified)

## Tasks
This project consists of several tasks, each building upon the knowledge gained from the previous ones. You are tasked with creating a class called `Square` and implementing various functionalities. Here are the tasks you need to complete:

1. **My First Square**
   - Write an empty class `Square` that defines a square.
   - You are not allowed to import any modules.
   
2. **Square with Size**
   - Write a class `Square` that defines a square with a private instance attribute `size`.
   - Instantiate the square with a size (no type/value verification).
   - You are not allowed to import any modules.

3. **Size Validation**
   - Write a class `Square` that defines a square with a private instance attribute `size`.
   - Instantiate the square with an optional size and perform size validation:
     - `size` must be an integer; otherwise, raise a `TypeError` exception with the message: "size must be an integer."
     - If `size` is less than 0, raise a `ValueError` exception with the message: "size must be >= 0."
   - You are not allowed to import any modules.

4. **Area of a Square**
   - Write a class `Square` that defines a square with a private instance attribute `size`.
   - Instantiate the square with an optional size and perform size validation.
   - Implement a public instance method `area` that returns the current square area.
   - You are not allowed to import any modules.

5. **Access and Update Private Attribute**
   - Write a class `Square` that defines a square with a private instance attribute `size`.
   - Implement a property to retrieve the `size`.
   - Implement a property setter to set the `size` and perform size validation:
     - `size` must be an integer; otherwise, raise a `TypeError` exception with the message: "size must be an integer."
     - If `size` is less than 0, raise a `ValueError` exception with the message: "size must be >= 0."
   - Instantiate the square with an optional size.
   - Implement a public instance method `area` that returns the current square area.
   - You are not allowed to import any modules.

6. **Printing a Square**
   - Write a class `Square` that defines a square with private instance attributes `size` and `position`.
   - Implement a property to retrieve the `size`.
   - Implement a property setter to set the `size` and perform size validation.
   - Implement a property to retrieve the `position`.
   - Implement a property setter to set the

