#!/usr/bin/env python3
def uppercase(str):
    for i in range(0, len(str)):
        x = ord(str[i])
        if x >= 97 and x <= 122:
            x = x-32
        y = chr(x)
        print(y, end="")
