#!/usr/bin/python3
"""  takes in a URL and an email address, sends a POST request"""

if __name__ == '__main__':

    import requests
    import sys

    data = {"email": sys.argv[2]}

    respond = requests.post(sys.argv[1], data=data)
    print(respond.text)
