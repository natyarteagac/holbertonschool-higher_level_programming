#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except TypeError as err:
        print("Unknown format code 'd' for object of type 'str'".format(err))
        return False
    except ValueError:
        pass
