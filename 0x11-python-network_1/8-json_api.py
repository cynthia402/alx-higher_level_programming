#!/usr/bin/python3
""" takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_userwith the letter as a parameter."""
import requests
import sys

if __name__ == '__main__':
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}

    url = "http://0.0.0.0:5000/search_user"
    respond = requests.post(url, data=data)

    try:
        j_data = respond.json()
        if j_data:
            print("[{}] {}".format(j_data.get('id'), j_data.get('name')))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
