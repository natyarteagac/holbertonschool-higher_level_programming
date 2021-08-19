#!/bin/bash
# Sending the status request.
curl -o -I -L -s -w "%{http_code}" "$1"
