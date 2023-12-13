"""
a python file for question no. 8
"""
class BaseGeometry():
    """
    a class
    """
    def area(self):
        """
        Public instance method, that raises an Exception with the message: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method, that validates value.
        you can assume name is always a string
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    rectangle class
    """
    def __init__(self, width, height):
        """
        init method
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        the_area = self.__height * self.__width
        return the_area
    
    def __str__(self):
        result = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return result
    
class Square(Rectangle):
    """
    square class
    """
    def __init__(self, size):
        """
        init method
        """
        super().__init__()
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        the_area = self.__size * self.__size
        return the_area