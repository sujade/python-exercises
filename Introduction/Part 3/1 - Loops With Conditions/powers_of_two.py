#Please write a program which asks the user to type in an upper limit. The program then prints out numbers so that each subsequent number is the previous one doubled, starting from the number 1. That is, the program prints out powers of two in order.

num = int(input("Upper limit: "))
start = 1

while start <= num:
    print(start)
    start *= 2