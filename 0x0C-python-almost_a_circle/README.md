# Almost a Circle

## Introduction
The "Almost a Circle" project is part of the Higher-Level Programming curriculum and focuses on reinforcing Python concepts such as object-oriented programming, unit testing, serialization, and working with JSON. The project involves the implementation of classes and methods related to rectangles and squares.

## Getting Started
These instructions will help you set up the project on your local machine for development and testing purposes.

### Prerequisites
- Python 3.8.5
- Pycodestyle (version 2.8.*)

### Installing
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/almost-a-circle.git ```

2. Navigate the project directory:
   ```bash
   cd almost-a-circle
   ```
3. Create a virtual environment (optional but recommended):
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Project Structure
```
almost-a-circle/
│
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── rectangle.py
│   └── square.py
│
├── tests/
│   ├── __init__.py
│   ├── test_models/
│   │   ├── __init__.py
│   │   ├── test_base.py
│   │   ├── test_rectangle.py
│   │   └── test_square.py
│   └── ...
│
├── README.md
├── requirements.txt
└── your_script.py
```

### Running the Tests
Ensure that you are in the project root directory and run the following command to execute all unit tests:

```bash
python3 -m unittest discover tests
```

### Resources

args/kwargs ("https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/"
JSON encoder and decoder
unittest module
Python test cheatsheet

### Usage
You can use the provided example script (your_script.py) as a starting point to interact with the implemented classes. Modify the script according to your needs.


