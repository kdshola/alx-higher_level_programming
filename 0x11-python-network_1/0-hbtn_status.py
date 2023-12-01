#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    from urllib import request
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        content = response.read()
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")
