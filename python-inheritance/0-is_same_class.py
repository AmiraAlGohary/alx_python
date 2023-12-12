"""
a python file for question no. 0
"""
# def is_same_class(obj, a_class):
#     """
#     a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
#     """
#     if a_class == object:
#         return False
#     elif type(obj) == bool:
#         return False
#     else:
#         class_name = type(obj)
#         if issubclass(class_name, a_class):
#             return True
#         else:
#             return False


def is_same_class(obj, a_class):
    """
    a function that returns True if the object is exactly an instance of the specified class ; otherwise False.
    """
    return type(obj) is a_class