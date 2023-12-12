"""
a python file for question no. 1
"""

def is_kind_of_class(obj, a_class):
    """
    a function that returns True:
    - if the object is an instance of the specified class, or
    - if the object is an instance of a class that inherited from the specified class;
    
    otherwise False.
    """
    if issubclass(obj, a_class):
        return True
    else:
        return False
