#!/usr/bin/python3
"""post email with urlli """
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":

    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode()
    url = sys.argv[1]
    with urllib.request.urlopen(url, data) as response:
        cont = response.read().decode("utf-8")
        print(cont)
