import random

numb1 = random.randint(0, 1000)
numb2 = random.randint(0, 1000)

print(f"  {numb1}\n+ {numb2}")

print("Enter answer: ", end="")
answer = int(input())

if answer == numb1 + numb2:
    print("Congrat")
else:
    print(f"Incorrect\nCorrect answer: {numb1+numb2}")
