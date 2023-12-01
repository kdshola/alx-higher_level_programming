#!/usr/bin/python3
""" Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id """

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys
    name = sys.argv[1]
    passwd = sys.argv[2]
    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(name, passwd)
    response = requests.get(url, auth=auth)
    print(response.json().get('id'))
