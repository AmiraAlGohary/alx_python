"""
a python file for question no. 2
"""

def inherits_from(obj, a_class):
    """
    a function that returns True:
    - if the object is an instance of a class that inherited (directly or indirectly) from the specified class;    
    otherwise False.
    """
    
    if issubclass(type(obj), a_class):
        if isinstance(obj, a_class):
            return False
        else:
            return True
    else:
        return False