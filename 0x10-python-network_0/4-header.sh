#!/bin/bash
# takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. Header variable X-School-User-Id is sent with the value 98
curl -sH "X-School-User-Id: 98" "$1"
