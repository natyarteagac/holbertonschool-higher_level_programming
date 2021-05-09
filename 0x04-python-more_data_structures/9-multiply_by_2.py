#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    [value * 2 for value in new_dictionary]
    return new_dictionary
