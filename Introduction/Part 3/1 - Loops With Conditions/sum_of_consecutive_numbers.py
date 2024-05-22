#Please write a program which asks the user to type in a limit. The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) until the sum is at least equal to the limit set by the user.

limit = int(input("Limit: "))
total_sum = 0
current_number = 1

while total_sum < limit:
    total_sum += current_number
    current_number += 1

print(total_sum)