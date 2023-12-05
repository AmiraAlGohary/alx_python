def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    Returns a new matrix:
        Same size as matrix
        Each value should be the square of the value of the input
    """
    new_matrix_list = []
    for element in matrix:
        new_element = list(map((lambda x: x**2), element))
        new_matrix_list.append(new_element)
    return new_matrix_list