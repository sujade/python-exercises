#Please write a program which asks the user for three letters. The program should then print out whichever of the three letters would be in the middle if the letters were in alphabetical order.

first_letter = input("1st letter: ")
second_letter = input("2nd letter: ")
third_letter = input("3rd letter: ")

if first_letter < second_letter < third_letter or third_letter < second_letter < first_letter:
    middle_letter = second_letter
elif second_letter < first_letter < third_letter or third_letter < first_letter < second_letter:
    middle_letter = first_letter
else:
    middle_letter = third_letter

print(f"The letter in the middle is {middle_letter}")
