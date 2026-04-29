import random

print("Welcome to the Cows and Bulls Game!")
rand = [str(random.randint(0, 9)) for _ in range(4)]
while True:
    cows = 0
    guess = list(input("Enter a number: "))

    for i in range(4):
        if guess[i] == rand[i]:
            cows += 1

    bulls = sum(min(guess.count(d), rand.count(d)) for d in set(guess)) - cows

    print(f"{cows} cows, {bulls} bulls")

    if guess == rand:
        print("Correct")
        break
