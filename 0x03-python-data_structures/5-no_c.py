#!usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    count_lower = my_string.count('c')
    count_upper = my_string.count('C')
    while count_lower > 0:
            my_string.remove('c')
            count_lower -= 1
    while count_upper > 0:
            my_string.remove('C')
            count_upper -= 1
    return "".join(my_string)
