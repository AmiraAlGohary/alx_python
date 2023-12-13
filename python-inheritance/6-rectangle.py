"""
a python file for question no. 6
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
    def __init__(self, width, height):
        """
        init method
        """
        self.__width = width
        self.__height = height

    def integer_validator(self, width, height):
        """
        Public instance method, that validates width & height.
        """
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format(width))
        if width <= 0:
            raise ValueError("{} must be greater than 0".format(width))
        
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format(height))
        if height <= 0:
            raise ValueError("{} must be greater than 0".format(height))



