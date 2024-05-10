#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id """

if __name__ == '__main__':
    import sys
    from urllib.request import urlopen

    with urlopen(sys.argv[1]) as response:
        header = response.getheader('X-Request-Id')
        print(header)
