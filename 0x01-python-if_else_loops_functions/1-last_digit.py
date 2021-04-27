#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_number = number % -10
else:
    last_number = number % 10
str = "Last digit of {:d} is {:d}".format(number, last_number)
if last_number > 5:
    print("{0} and is greater than 5".format(str))
elif last_number == 0:
   print("{0} and is 0".format(str))
elif last_number < 6 & last_number != 0:
	print("{0} and is less than 6 and not 0".format(str))
