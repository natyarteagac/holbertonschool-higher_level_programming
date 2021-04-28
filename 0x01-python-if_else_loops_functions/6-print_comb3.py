#!/usr/bin/python3
i = 0
n = 0
for i in range(10):
    for n in range(i + 1, 10):
            if i == 8 and n == 9:
                print("{}{}\n".format(i, n), end='')
            else:
                print("{0}{1}".format(i, n), end='')
                print(", ".format(i, n), end='')
