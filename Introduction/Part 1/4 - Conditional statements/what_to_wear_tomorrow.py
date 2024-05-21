##Please write a program which asks for tomorrow's weather forecast and then suggests weather-appropriate clothing.

##The suggestion should change if the temperature (measured in degrees Celsius) is over 20, 10 or 5 degrees, and also if there is rain on the radar.

temp = int(input("Temperature:"))
rain = input("Will it rain (yes/no):")

if temp > 20:
    print("Wear jeans and a T-shirt")
elif temp >10:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well")
elif temp > 5:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you")
else:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order")

if rain == "yes":
    print("Don't forget your umbrella!")