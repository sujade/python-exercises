##Please write a program which prints out the following story. The user gives a name and a year, which should be inserted into the printout.

##Sample output
##Please type in a name: Mary
##Please type in a year: 1572

##Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.

name = input("Please type a name:")
year = int(input("Please type in a year:"))

print(name + " was a valiant knight, born in the year " + year + ". One morning " + name + " woke up to an awful racket: a dragon was approaching the village. Only " + name + " could save the village's residents.")