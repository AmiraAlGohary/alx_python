"""
a python file for rectangle
"""

from models.base import Base 
# from base import Base

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

    def area(self):
        """
        a method that returns the area of the rectangle
        """
        the_area = self.__height * self.__width
        return the_area
    
    def display(self):
        """
        a method the prints the rectangle in # signs
        """
        the_width = self.__width
        the_height = self.__height
        x = self.__x
        y = self.__y
        drawn_width = x*" " + the_width*"#"
        
        for i in range(y):
            print("")
        for i in range(the_height):
            print(drawn_width)

    def __str__(self):
        """
        a rectangle print method
        """
        result = "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - " + str(self.width) + "/" + str(self.height)
        return result

    def update(self, *args):
        """
        a public method that assigns an argument to each attribute
        """
        if len(args) >=1:
            self.id = args[0]
        if len(args) >=2:
            self.__width = args[1]
        if len(args) >=3:
            self.__height = args[2]
        if len(args) >=4:
            self.__x = args[3]
        if len(args) >=5:
            self.__y = args[4]