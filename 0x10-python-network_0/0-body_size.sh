#!/bin/bash
# Script that takes in a URL, sends a request to
# that URL

curl -sI "$2" | grep -i Content-Length | awk '{print $2}'
