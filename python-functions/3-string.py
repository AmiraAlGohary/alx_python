def reverse_string(string):
    result = ""
    for i in string:
        result = i + result
    return result