"""
a python file for question no. 3
"""

# class MetaClass(object):
#     """
#     a class to override the init_subclass attribute
#     """
#     def dir(cls):
#         return [attribute for attribute in super().dir() if attribute != "__init_subclass__"]

class BaseGeometry():
    """
    a class
    """
    def area(self):
        """
        Public instance method, that raises an Exception with the message: area() is not implemented
        """
        raise Exception("area() is not implemented")



