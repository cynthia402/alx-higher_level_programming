#!/usr/bin/python3
"""Thisinherits from the list class"""
class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
