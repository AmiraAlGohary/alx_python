for i in range(100):
    if i <10:
        print(str(0) + str(i), end=", ")
    elif i == 99:
        print(i)
    else:
        print(str(i), end=", ")