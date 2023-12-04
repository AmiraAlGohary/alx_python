def raise_exception():
    try:
        result = "1" + 11
    except TypeError as te:
        print("Exception raised")