#!/usr/bin/python3
""" Python script that takes 2 arguments. Prings 10 latest commits """

if __name__ == "__main__":
    import requests
    import sys
    url = f'https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits'
    response = requests.get(url)
    try:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit.get("sha")
            name = commit.get("commit").get("author").get("name")
            print(f'{sha}: {name}')
    except IndexError:
        pass
