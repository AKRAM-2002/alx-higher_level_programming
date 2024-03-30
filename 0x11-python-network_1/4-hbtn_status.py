#!/usr/bin/python3
# script that fetches https://alx-intranet.hbtn.io/status using requests package

import requests
if __name__ == "__main__":

    url = 'https://alx-intranet.hbtn.io/status'
    with requests.get(url) as res:
        html = res.text
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)

