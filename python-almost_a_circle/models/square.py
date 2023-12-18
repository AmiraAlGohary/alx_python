"""
a python file for square
"""

# from models.rectangle import Rectangle 
from rectangle import Rectangle

class Square(Rectangle):
    """
    a Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init method
        """
        super().__init__(self, size, size, x=0, y=0, id=None)
        