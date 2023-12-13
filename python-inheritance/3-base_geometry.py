"""
a python file for question no. 3
"""

class MyMeta(type):
    """
    a metaclass to override the init_subclass attribute
    """
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

class BaseGeometry(metaclass=MyMeta):
    """
    an empty class
    """
    pass

# class BaseGeometry:
#     """
#     an empty class
#     """
#     def dir(cls):
#         return [attribute for attribute in super().dir() if attribute != "__init_subclass__"]