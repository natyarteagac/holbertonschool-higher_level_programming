#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx + 1 > len(my_list):
        return my_list
    elif idx + 1 < len(my_list):
        my_list.remove(idx + 1)
        my_list.insert(idx, element)
