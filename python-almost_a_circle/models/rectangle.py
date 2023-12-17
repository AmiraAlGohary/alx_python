"""
a python file for rectangle
"""

from models.base import Base 

# class Base:
#     """
#     a Base class
#     """
#     __nb_objects = 0
#     def __init__(self, id=None):
#         """
#         init method
#         """
#         if id != None:
#             self.id = id
#         else:
#             Base.__nb_objects +=1
#             self.id = Base.__nb_objects

class Rectangle(Base):
    """
    a Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(id)
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
        self.__y = y
