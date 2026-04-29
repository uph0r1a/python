import random

lottery_numbers = []

for _ in range(7):
    lottery_numbers.append(random.randint(0, 9))

for number in lottery_numbers:
    print(number, end=" ")
