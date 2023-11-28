def fibonacci_sequence(n):
    if n == 0 or n == 1:
        result = 1
    elif n > 1:
        result = fibonacci_sequence(n-1) + fibonacci_sequence(n-2)

    return result
print(fibonacci_sequence(4))