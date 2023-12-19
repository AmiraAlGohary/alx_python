"""
a python file for square
"""

from models.rectangle import Rectangle 
# from rectangle import Rectangle

class Square(Rectangle):
    """
    a Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(size, size, x, y, id)
        self.size = size


    def __str__(self):
        """
        a square print method
        """
        result = "[Square] (" + str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - " + str(self.width)
        return result
    
    @property
    def size(self):
        """
        a getter for size
        """
        return self.size
    
    @size.setter
    def size(self, size):
        """
        a setter for size
        """
        if not isinstance(size, int):
            raise TypeError("{} must be an integer".format("width"))
        if size <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.size = size





