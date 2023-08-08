#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit_num = abs(number) % 10
if number < 0:
    last_digit_num = -last_digit_num
if last_digit_num > 5:
    str = "and is greater than 5"
elif last_digit_num == 0:
    str = "and is 0"
else:
    str = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit_num} {str}")
