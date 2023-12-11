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

    def area(self):
        """
        a method used for calculating the area of the square
        """
        square_area = self.__size * self.__size
        return square_area
    
    @property
    def size(self):
        """
        a method used for retrieving the size
        """
        return self.__size
    
    @size.setter
    def size(self, value):
        """
        a method used for setting the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        a method used for printing the square with # signs
        """
        if self.__size == 0:
            print("\n")
        elif self.__size > 0:
            side_lenght = self.__size
            drawn_square_line = side_lenght*"#"
            for i in range(side_lenght):
                print(drawn_square_line)