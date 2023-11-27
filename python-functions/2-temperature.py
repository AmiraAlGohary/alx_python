def convert_to_celsius(fahrenheit):
    Celsius = (fahrenheit - 32)*(5/9)
    return float(Celsius)

print(convert_to_celsius(100))
print(convert_to_celsius(-40))
print(convert_to_celsius(-459.67))
print(convert_to_celsius(32))


# from decimal import Decimal, getcontext

# def convert_to_celsius(fahrenheit):
#     getcontext().prec = 4  # Set the precision to 4 decimal places
#     celsius = (Decimal(fahrenheit) - Decimal('32')) * Decimal('5') / Decimal('9')
#     return float(celsius)  # Convert back to float before returning

# result = convert_to_celsius(-459.67)
# print(result)