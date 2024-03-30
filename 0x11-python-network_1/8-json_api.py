#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
    Otherwise:
    Display Not a valid JSON if the JSON is invalid
    Display No result if the JSON is empty
"""



if __name__ == "__main__":
    import sys
    import requests

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': sys.argv[1] if len(sys.argv) >= 2 else ""}

    res = requests.post(url, data=data)
    type_res = res.headers['content-type']

    if type_res == 'application/json':
        result = res.json()
        _id = result.get('id')
        name = result.get('name')
        if (result != {} and _id and name):
            print("[{}] {}".format(_id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')