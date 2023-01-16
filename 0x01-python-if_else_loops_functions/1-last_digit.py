#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(rep(number)[-10])
print(f"the last_digit of {number} is {last_digit}")
if last_digit > 5:
    print(f"last digit of {number} is greater than 5")
elif last_digit == 0:
    print(f"last digit of {number} is zero")
elif last_digit < 6 and not 0:
    print(f"\"last digit of {number} is {last_digit} and is less than 6 and not 0")
