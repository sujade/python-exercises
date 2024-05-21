##Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

temp = float(input("Please type in a temperature."))
cel = (temp - 32) * 5/9

if cel < 0:
    print(f"{temp} degrees Fahrenheit equals {cel} degrees Celsius\nBrr! It's cold in here!")
else:
    print(f"{temp} degrees Fahrenheit equals {cel} degrees Celsius")