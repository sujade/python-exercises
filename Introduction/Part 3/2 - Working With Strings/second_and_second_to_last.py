#Please write a program which asks the user for a string. The program then prints out a message based on whether the second character and the second to last character are the same or not. See the examples below.

str = input("Please type in a string: ")
if str[1] == str[-2]:
    print("The second and the second to last characters are " + str[1])
else:
    print("The second and the second to last characters are different")