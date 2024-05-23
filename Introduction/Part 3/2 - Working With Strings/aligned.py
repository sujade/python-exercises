#Please write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

user_input = input("Please type in a string: ")
num_stars = 20 - len(user_input)
padded_string = '*' * num_stars + user_input
print(padded_string)