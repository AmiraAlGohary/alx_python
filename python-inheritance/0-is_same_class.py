"""
a python file for question no. 0
"""


def is_same_class(obj, a_class):
    """
    a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False