##Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.

wage = float(input("Hourly wage:"))
hours = int(input("Hours worked:"))
day = input("Day of the week:")

wage_total = wage * hours
weekend_wage_total = wage_total * 2

if day == "Sunday":
    print(f"Daily wages: {weekend_wage_total} euros")
else:
    print(f"Daily wages: {wage_total} euros")