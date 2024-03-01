#!/usr/bin/python3
""" contain inhertied class defination"""
from models.base import Base


class Rectangle(Base):
    """represent inherited class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance
        with the character # """
        for y in range(self.y):
            print()
        for h in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        return f"[Rectangle] ({self.id}) {self.x}/{self.y}"\
            f" - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ that assigns an argument to each attribute:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute"""
        if args:
            j = 0
            for arg in args:
                if j == 0:
                    if arg is None:
                        pass
                    else:
                        self.id = arg
                elif j == 1:
                    self.width = arg
                elif j == 2:
                    self.height = arg
                elif j == 3:
                    self.x = arg
                elif j == 4:
                    self.y = arg
                j += 1
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        pass
                    else:
                        self.id = value
                elif key == "height":
                    self.height = value
                elif key == "width":
                    self.width = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ that returns the dictionary representation of a Rectangle """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
