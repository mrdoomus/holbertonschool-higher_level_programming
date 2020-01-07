#!/bin/bash
# Takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | cut -f2 -d ' ' | tail -3 | head -1
