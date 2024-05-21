##Please write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

##You can assume all words will be typed in lowercase entirely.

word_one = input("Please type in the first word:")
word_two = input("Please type in the second word:")

if word_one > word_two:
    print(f"{word_one} comes alphabetically last.")
elif word_two > word_one:
    print(f"{word_two} comes alphabetically last.")
else:
    print("You gave the same word twice.")