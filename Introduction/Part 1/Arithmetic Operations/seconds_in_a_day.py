##Please write a program which asks the user for a number of days. The program then prints out the number of seconds in the amount of days given.

days = int(input("How many days?"))
res = days * 60 * 60 * 24

print(f"Seconds is that many days: {res}")