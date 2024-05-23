#!/usr/bin/python3
"""Module that contain class square"""


class Square():
    """
    square class

    -Attributes:
    length (int): the square length
    """

    def __init__(self, length=0):
        """initialization method"""
        self.length = length

    def area_of_my_square(self):
        """ Area of the square """
        return self.length * 2

    def perimeter_of_my_square(self):
        """perimeter of the square"""
        return self.length * 4

    def __str__(self):
        """string representation"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = Square(12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
