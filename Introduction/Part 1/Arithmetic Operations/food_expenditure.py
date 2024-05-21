##Please write a program which estimates a user's typical food expenditure.

##The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

##Based on this information the program calculates the user's typical food expenditure both weekly and daily.

##The program should function as follows:

##Sample output
##How many times a week do you eat at the student cafeteria? 4
##The price of a typical student lunch? 2.5
##How much money do you spend on groceries in a week? 28.5

##Average food expenditure:
##Daily: 5.5 euros
##Weekly: 38.5 euros

cafeteria_days = float(input("How many days do you eat at the student cafe?"))
lunch_price = float(input("The price of a typical student lunch?"))
groceries_price = float(input("How much money do you spend on groceries in a week?"))

weekly_expenses = (cafeteria_days * lunch_price) + groceries_price
daily_expenses = weekly_expenses / 7

print("Average food expenditure:")
print(f"Daily: {daily_expenses} euros")
print(f"Weekly: {weekly_expenses} euros")