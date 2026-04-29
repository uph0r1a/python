def dumb_guess():
    for i in range(100):
        print(i)
        while 1:
            check = input("Is this correct(Y/N): ").lower()
            if check == "y":
                print(f"Yippe\nNumber of guesses: {i + 1}")
                exit()
            elif check == "n":
                break
            else:
                print("Invalid choice")
    print("Hmm... Cheater")


def optimal_guess():
    low = 0
    high = 100
    count = 0

    while low <= high:
        count += 1
        middle = (high + low) // 2
        print(middle)

        while True:
            check = input("Is this too high, too low or correct: ").lower().strip()
            if check in {"too high", "too low", "correct"}:
                break
            print("Invalid choice")

        if check == "too high":
            high = middle - 1
        elif check == "too low":
            low = middle + 1
        else:
            print(f"Yippe\nNumber of guesses: {count}")
            return

    print("Hmm... Cheater")


input("Think of a number...")
optimal_guess()
