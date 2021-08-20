#!/usr/bin/python3
""" Test function find_pak """


def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    list_of_integers.sort()
    array_length = len(list_of_integers)
    last_number = list_of_integers[array_length - 1]
    return last_number
