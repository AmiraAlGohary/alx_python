for i in range(10):
    for j in range(10):
        if i == j:
            pass
        elif i > j:
            pass
        else:
            print("{}{}".format(i,j), end=", ")
