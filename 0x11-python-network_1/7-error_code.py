#!/usr/bin/python3
""" sends a request to the URL and displays the body of the response"""
import sys
import requests

if __name__ == '__main__':
    respond = requests.get(sys.argv[1])
    if respond.status_code >= 400:
        print("Error code:", respond.status_code)
    else:
        print(respond.text)
