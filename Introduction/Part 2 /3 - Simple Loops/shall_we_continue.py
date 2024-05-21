##This program should print out the message "hi" and then ask "Shall we continue?" until the user inputs "no". Then the program should print out "okay then" and finish.

print("hi")
answer = input("Shall we continue?")

while True:
    if answer.lower() == "no":
        break
    else:
        print("hi")
        answer = input("Shall we continue?")
        
print("okay then")