##Please write a program which asks the user for an integer number. The program should then print out the magnitude of the number.

num = int(input("Please type in a number:"))

if num < 10:
    print("This number is smaller than 1000\nThis number is smaller than 100\nThis number is smaller than 10\nThank you!")
elif num < 100:
    print("This number is smaller than 1000\nThis number is smaller than 100\nThank you!")
elif num < 1000:
    print("This number is smaller than 1000\nThank you!")
else:
    print("Thank you!")