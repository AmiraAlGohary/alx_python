"""
a python file to write the Square Class
"""


class Square():
    """
    a class that defines a square by private instance attribute: size
    """
    def __init__(self, size=0):
        """
        a method used for initializing instances
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size