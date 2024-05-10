#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest)"""

if __name__ == '__main__':
    import requests
    import sys

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    api_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        try:
            for i in range(10):
                print(data[i]['sha'], end=": ")
                print(data[i]['commit']['author']['name'])
        except IndexError as e:
            pass
    else:
        print(f"Error: {response.status_code}")
