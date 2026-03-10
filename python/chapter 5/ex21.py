import random

isWin = False
choice = ["rock", "paper", "scissors"]

while not isWin:
    computer = random.randint(0, 2)
    print("Enter your choice: ", end="")
    player = input().lower()

    if player not in choice:
        print("Invalid move\nComputer wins")
        isWin = True
        continue

    print(f"Computer choice: {choice[computer]}")

    if player == choice[computer]:
        print("Tie")
        isWin = True
    elif player == "rock" and choice[computer] == "paper":
        print("Computer wins")
        isWin = True
    elif player == "paper" and choice[computer] == "scissors":
        print("Computer wins")
        isWin = True
    elif player == "scissors" and choice[computer] == "rock":
        print("Computer wins")
        isWin = True
    else:
        print("Player wins")
        isWin = True
