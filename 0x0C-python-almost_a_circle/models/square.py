#!/usr/bin/python3
"""module that contains class defination """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ represent class defination"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """ return size"""
        return self.width

    @size.setter
    def size(self, value):
        """ set value to size"""
        self.width = value
        self.height = value

    def __str__(self):
        """ retrun formal presentation of instance """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """ update the instance arguments"""
        if args:
            len_args = 0
            for arg in args:
                if len_args == 0:
                    if arg is None:
                        pass
                    else:
                        self.id = arg
                elif len_args == 1:
                    self.size = arg
                elif len_args == 2:
                    self.x = arg
                elif len_args == 3:
                    self.y = arg
                len_args += 1
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if key is None:
                        pass
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle: """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
