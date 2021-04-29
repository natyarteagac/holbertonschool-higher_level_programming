#!/usr/bin/python3
if __name__ == "__main__":
    import sys
count = len(sys.argv)
number1 = 0
for i in range(1, count):
    number2 = int(sys.argv[i])
    number1 = number1 + number2
print("{:d}".format(number1))
