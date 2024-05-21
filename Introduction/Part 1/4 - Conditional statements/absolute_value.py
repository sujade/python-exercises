##Please write a program which asks the user for an integer number. If the number is less than zero, the program should print out the number multiplied by -1. Otherwise the program prints out the number as is.

num = float(input("Please type in a number:"))
absolute_minus = num * -1

if num < 0:
    print(f"The absolute of this number is {absolute_minus}")
else:
    print(f"The absolute value of this number is {num}")