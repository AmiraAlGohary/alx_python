def is_prime(number):
    """
    Returns True if the number is prime, and False otherwise.
    """
    if number < 2:
        return False
    elif number >=2:
        for i in range(2, number):
            if number%i == 0:
                return False
        return True