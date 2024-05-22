#Please write a program which asks the user for two strings and then prints out whichever is the longer of the two - that is, whichever has the more characters. If the strings are of equal length, the program should print out "The strings are equally long".

str1 = input("Please type in string 1: ")
str2 = input("Please type in string 2: ")

if len(str1) > len(str2):
    print(f"{str1} is longer")
elif len(str2) > len(str1):
    print(f"{str2} is longer")
else:
    print("The strings are equally long")