#!/bin/bash
# Script that takes in a URL, sends a request to
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
