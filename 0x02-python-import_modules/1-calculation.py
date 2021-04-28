#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    a = 10
    b = 5

    print("{} + {} = {}\n".format(a, b, add(a, b)), end='')

    from calculator_1 import sub
    print("{} - {} = {}\n".format(a, b, sub(a, b)), end='')

    from calculator_1 import mul
    print("{} * {} = {}\n".format(a, b, mul(a, b)), end='')

    from calculator_1 import div
    print("{} / {} = {}\n".format(a, b, div(a, b)), end='')
