#!/usr/bin/python3
"""Module that contain class square"""


class Square():
    """
    square class

    -Attributes:
    width: the square width
    height: the square height
    """

    def __init__(self, *args, **kwargs):
        """instantiation method"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """perimeter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """string representation"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """
    Test the class
    """

    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
