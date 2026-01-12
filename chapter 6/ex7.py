import random

print("Enter how many random numbers the file will hold: ", end="")
number = int(input())

with open("files/random.txt", "w") as f:
    for i in range(number):
        f.write(f"{random.randint(1,500)}\n")
