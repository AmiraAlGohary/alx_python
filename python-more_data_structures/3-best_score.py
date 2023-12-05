def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    If no score found, return None

    You can assume that all values are only integers
    You can assume all students have a different scores
    """
    # if a_dictionary == {}:
    #     return None
    # else:
    #     BiggestValue = max(list(a_dictionary.values()))
    #     for key in a_dictionary:
    #         if a_dictionary[key] == BiggestValue:
    #             thebest_score = key
    #     return thebest_score

    if a_dictionary == {}:
        return None
    else:
        biggestValue = 0
        newValue = 0

        for key in a_dictionary:
            newValue =  a_dictionary[key]
            if newValue > biggestValue:
                biggestValue = newValue
                thebest_score = key
        
        return thebest_score