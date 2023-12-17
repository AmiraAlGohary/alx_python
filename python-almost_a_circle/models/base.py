"""
a python file for base
"""

class Base:
    """
    a Base class
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """
        init method
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects +=1
            self.id = Base.__nb_objects