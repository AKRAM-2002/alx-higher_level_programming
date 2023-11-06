# 0x0A. Python - Inheritance

**Project By: Guillaume**

**Weight: 1**

**Project Start Date: Nov 6, 2023 4:00 AM**

**Project End Date: Nov 7, 2023 4:00 AM**

**Checker Release Date: Nov 6, 2023 10:00 AM**

**Auto Review Deadline: Project deadline**

## Resources

Read or watch:

- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://docs.python.org/3/tutorial/classes.html#multiple-inheritance)
- [Inheritance in Python](https://www.tutorialspoint.com/python/python_inheritance.htm)
- [Learn to Program 10: Inheritance Magic Methods](https://www.youtube.com/watch?v=0oTh1CXRaQ0)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
- Why Python programming is awesome
- What is a superclass, base class, or parent class
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when, and how to use `isinstance`, `issubclass`, `type`, and `super` built-in functions

## Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

**Python Scripts**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

**Python Test Cases**
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: .txt)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Documentation

- Do not use the words `import` or `from` inside your comments, the checker will think you try to import some modules

## Tasks

### 0. Lookup

- Write a function that returns the list of available attributes and methods of an object:

```python
Prototype: def lookup(obj):
Returns a list object
You are not allowed to import any module
```


### 1. My List
- Write a class MyList that inherits from list:

```python
Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module
```

### 2. Exact Same Object
- Write a function that returns True if the object is exactly an instance of the specified class; otherwise False.
```python
Prototype: def is_same_class(obj, a_class)
You are not allowed to import any module
```

### 3.Same Class or inherit From
- Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.
````python
Prototype: def is_kind_of_class(obj, a_class)
You are not allowed to import any module
```

### 4.Only Subclass Of
-Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.
```python
Prototype: def inherits_from(obj, a_class)
You are not allowed to import any module
```

### 5.Geometry Module
-Write an empty class BaseGeometry.
```python
You are not allowed to import any module
```

### 6.Improve Geometry
-Write a class BaseGeometry (based on 5-base_geometry.py)
```python
Public instance method: def area(self): that raises an Exception with the message area() is not implemented
You are not allowed to import any module
```

### 7.Integer Validator
-Write a class BaseGeometry (based on 6-base_geometry.py).

```python
Public instance method: def area(self): that raises an Exception with the message area() is not implemented
Public instance method: def integer_validator(self, name, value): that validates value:
You can assume name is always a string
If value is not an integer: raise a TypeError exception, with the message <name> must be an integer
If value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0
You are not allowed to import any module
```
