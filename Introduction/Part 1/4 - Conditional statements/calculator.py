##Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, the program should calculate and print out the result of the operation with the given numbers. If the user types in anything else, the program should print out nothing.

num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
operation = input("Operation:")
res_add = num1 + num2
res_substract = num1 - num2
res_multiply = num1 * num2

if operation == "add":
    print(f"{num1} + {num2} = {res_add}")
elif operation == "subtract":
    print(f"{num1} - {num2} = {res_substract}")
elif operation == "multiply":
    print(f"{num1} * {num2} = {res_multiply}")