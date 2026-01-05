import random


def checkNumber(number, guess):
    if guess > number:
        print("Too high, try again")
    elif guess < number:
        print("Too low, try again")
    else:
        print("Congrat")


choice = ""
guess = None

while choice.lower() != "no":
    count = 0
    number = random.randint(1, 100)
    while number != guess:
        print("Enter your guess: ", end="")
        guess = int(input())
        checkNumber(number, guess)
        count += 1
    print(f"Number of guesses: {count}\nDo you want to continue: ", end="")
    choice = input()
