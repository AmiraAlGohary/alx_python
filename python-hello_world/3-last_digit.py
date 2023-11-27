#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
stringNumber = str(number)

lastDigit = stringNumber[-1]
lastDigit = int(lastDigit)

if number < 0:
    lastDigit = - lastDigit

if lastDigit > 5:
    print("Last digit of " + str(number) + " is " + str(lastDigit) + " and is greater than 5" )

elif lastDigit == 0:
    print("Last digit of " + str(number) + " is " + str(lastDigit) + " and is 0")

elif lastDigit < 6:
    print("Last digit of " + str(number) + " is " + str(lastDigit) + " and is less than 6 and not 0")
else:
    pass