def multiply_list_map(my_list=[], number=0):
    new_List = list(map((lambda x: x*(number)), (my_list)))
    return new_List