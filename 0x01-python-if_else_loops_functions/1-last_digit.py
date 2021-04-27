#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_number = number % -10
else:
    last_number = number % 10
str = "Last digit of {0} is {1}".format(number, last_number)
if last_number > 5:
    print("{0} and is greater than 5".format(str), end='')
elif last_number == 0:
   print("{0} and is 0".format(str), end='')
elif last_number < 6 and last_number != 0:
	print("{0} and is less than 6 and not 0".format(str), end='')
