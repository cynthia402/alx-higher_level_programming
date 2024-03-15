#!/usr/bin/python3
""" module define rectangle """


class Rectangle():
    """ define rectangle class """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ retrive value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retrive value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set value to height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ define area of rectangel"""
        return self.__height * self.__width

    def perimeter(self):
        """ return pwrimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")

        my_rect = []
        for i in range(self.__height):
            [my_rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                my_rect.append("\n")
        return ("".join(my_rect))

    def __repr__(self):
        """Return the string representation of Rectangle."""
        my_rect = "Rectangle(" + str(self.__width)
        my_rect += ", " + str(self.__height) + ")"
        return (my_rect)

    def __del__(self):
        """ delete the class rectangle """
        print("Bye rectangle...")
        del self
        Rectangle.number_of_instances -= 1
