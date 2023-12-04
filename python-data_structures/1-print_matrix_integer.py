def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j == i[-1]:
                print("{:d}".format(j), end="\n")
            else:
                print("{:d}".format(j), end=" ")

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(print_matrix_integer(matrix))