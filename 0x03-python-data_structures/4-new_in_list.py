#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    old_list = my_list.copy()
    if idx < 0:
        return old_list
    elif idx + 1 > len(my_list):
        return old_list
    else:
        new_list.remove(idx + 1)
        new_list.insert(idx, element)
        return new_list
