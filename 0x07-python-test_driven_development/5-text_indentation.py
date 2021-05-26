#!/usr/bin/python3
"""

    Function that print a text with 2 new lines after each of
    these characters: ., ? and :
"""


def text_indentation(text):
    """
    Printing with indentation
    """

    if type(text) != str:
        raise TypeError('text must be a string')

    text = text.replace('. ', '.\n\n')
    text = text.replace('? ', '?\n\n')
    text = text.replace(': ', ':\n\n')
    print(text, end='')
