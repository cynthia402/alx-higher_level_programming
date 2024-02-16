#!/usr/bin/python3
""" define a function that print size times '#' square"""


def print_square(size):
    """ function that print '#' square """

    if size is None:
        raise TypeError("print_square() missing 1\
            required positional argument: 'size'")
    if size is isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("{}".format('#' * size))
