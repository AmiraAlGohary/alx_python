def multiply_list_map(my_list=[], number=0):
    """
    Returns a new list with all values multiplied by a number without using any loops.
    Returns a new list:
        Same length as my_list
        Each value should be multiplied by number
    Initial list should not be modified
    """
    new_List = list(map((lambda x: x*(number)), (my_list)))
    return new_List