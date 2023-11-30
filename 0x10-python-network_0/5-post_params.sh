#!/bin/bash
# Takes in a URL, sends a POST request to it, and displays the body of the response with variables email=test@gmail.com and subject = I will always be here for PLD.
curl -X POST -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
