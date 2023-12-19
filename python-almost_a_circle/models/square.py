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


    def __str__(self):
        """
        a square print method
        """
        result = "[Square] (" + str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - " + str(self.width)
        return result