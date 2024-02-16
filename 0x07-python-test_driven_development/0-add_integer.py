#!/usr/bin/python3
""" define function
that add tw0 numbers"""


def add_integer(a, b=98):
    """Adds two integers and returns their sum.
    Args:
        a (int): The first integer to be added.
        b (int): The second integer to be added.
    Returns (int): The sum of the two integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
