#Please write a program which asks the user for a password. The program should then ask the user to type in the password again. If the user types in something else than the first password, the program should keep on asking until the user types the first password again correctly.

pw = input("Password")

while True:
    rp = input("Repeat password:")

    if pw != rp:
        print("They do not match!")
    else:
        print("User account created!")
        break