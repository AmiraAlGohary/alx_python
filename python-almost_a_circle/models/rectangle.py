"""
a python file for rectangle
"""

from models.base import Base 

class Rectangle(Base):
    """
    a Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format("width"))
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format("height"))
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format("x"))
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))

        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.__id = id

    @property
    def width(self):
        """
        a getter for width
        """
        return self.__width
    
    @width.setter
    def width(self, width):
        """
        a setter for width
        """
        if not isinstance(width, int):
            raise TypeError("{} must be an integer".format("width"))
        if width <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = width
    
    @property
    def height(self):
        """
        a getter for height
        """
        return self.__height
    
    @height.setter
    def height(self, height):
        """
        a setter for height
        """
        if not isinstance(height, int):
            raise TypeError("{} must be an integer".format("height"))
        if height <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = height
    
    @property
    def x(self):
        """
        a getter for x
        """
        return self.__x
    
    @x.setter
    def x(self, x):
        """
        a setter for x
        """
        if not isinstance(x, int):
            raise TypeError("{} must be an integer".format("x"))
        if x < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = x
    
    @property
    def y(self):
        """
        a getter for y
        """
        return self.__y
    
    @y.setter
    def y(self, y):
        """
        a setter for y
        """
        if not isinstance(y, int):
            raise TypeError("{} must be an integer".format("y"))
        if y < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = y
