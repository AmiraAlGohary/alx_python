def update_dictionary(a_dictionary, key, value):
    """
    A function that replaces or adds key/value in a dictionary
    
    Key argument will be always a string
    Value argument will be any type
    
    If a key exists in the dictionary, the value will be replaced
    If a key doesn’t exist in the dictionary, it will be created
    """
    if key in a_dictionary:
        a_dictionary[key] = value

    else:
        a_dictionary[key] = value