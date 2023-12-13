"""
a python file for question no. 3
"""

class MyMeta(type):
    """
    a metaclass to override the init_subclass attribute
    """
    def __dir__(cls):
        all_attrs = dir(type(cls))
        return [attribute for attribute in all_attrs if attribute != "__init_subclass__"]
    

class BaseGeometry(metaclass=MyMeta):
    """
    an empty class
    """
    pass

# def __init_subclass__(cls, **kwargs):
#     super().__init_subclass__(**kwargs)

# class BaseGeometry:
#     """
#     an empty class
#     """
#     def dir(cls):
#         return [attribute for attribute in super().dir() if attribute != "__init_subclass__"]