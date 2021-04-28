#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    a = 10
    b = 5

    print(a, '+', b, '=', add(a, b), '\n', end='')

    from calculator_1 import sub

    print(a, '-', b, '=', sub(a, b), '\n', end='')

    from calculator_1 import mul
    print(a, '*', b, '=', mul(a, b), '\n', end='')

    from calculator_1 import div
    print(a, '/', b, '=', div(a, b), '\n', end='')
