#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8) """

if __name__ == "__main__":
    from urllib import request
    from urllib import parse
    import sys
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    data = parse.urlencode(email).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
