def fibonacci_sequence(n):
    """
    Takes a number n as input
    Returns a list of the first n Fibonacci numbers.
    Return an empty list if the it is not possible to generate the Fibonacci numbers for n
    """
    def fibonacci_of(n):
        if n == 0 or n == 1:
            result = n
        else:
            result = fibonacci_of(n-1) + fibonacci_of(n-2)
        return result

    resulted = []
    if n =<0:
        return resulted
    elif n == 1:
        resulted = [0]
        return resulted
    elif n == 2:
        resulted = [0, 1]
        return resulted
    elif n > 2:
        resulted = [0, 1]
        for i in range(3, n+1):
            resulted.append(fibonacci_of(i-1))
        return resulted