#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter. """

if __name__ == "__main__":
    import requests
    import sys
    url = 'http://0.0.0.0:5000/search_user'
    letter = '' if len(sys.argv) == 1 else sys.argv[1]
    response = requests.post(url, data={'q': letter})
    try:
        response = response.json()
        if response:
            print(f"[{response.get('id')}] {response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
