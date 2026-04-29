import random, sys, os

while 1:
    os.system("clear")
    number = 0
    rand = random.randint(1, 9)
    while 1:
        number += 1
        guess = input("Guess the number: ")
        if guess.lower().strip() == "exit":
            sys.exit()
        elif not guess.isdigit():
            print("Invalid choice")
            number -= 1
        elif int(guess) > rand:
            print("Too high")
        elif int(guess) < rand:
            print("Too low")
        else:
            print(f"Correct\nNumber of guesses: {number}")
            break
    input("Press Enter to continue...")
