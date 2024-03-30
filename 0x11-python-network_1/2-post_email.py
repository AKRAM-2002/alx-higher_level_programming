#!/usr/bin/python3
# script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter
import sys
from  urllib import request, parse

if __name__ == "__main__":
    
    data = parse.urlencode({'email': sys.argv[2]})
    data = data.encode('utf-8')
    req = request.Request(sys.argv[1], data=data, method='POST')
    with request.urlopen(req) as response:
        html = response.read().decode('utf-8')
        print(html)



