"""
a python file for question no. 3
"""

class MetaClass:
    """
    a class to override the init_subclass attribute
    """
    def dir(cls):
        return [attribute for attribute in super().dir() if attribute != "__init_subclass__"]

class BaseGeometry(MetaClass):
    """
    an empty class
    """
    pass