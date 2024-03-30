#!/usr/bin/python3
""" Sends a request to the URL and displays the value of the variable X-Request-I"""

import sys
from requests import get


if __name__ == "__main__":

    url = sys.argv[1]
    res = get(url)
    print(res.headers['X-Request-Id'])
