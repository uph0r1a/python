valid = {"rock", "paper", "scissors"}
win = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

while 1:
    player1 = input("Player 1: ").lower().strip()
    player2 = input("Player 2: ").lower().strip()

    if player1 in valid and player2 in valid:
        if player1 == player2:
            print("Tie")
        elif win[player1] == player2:
            print("Player 1 win")
        else:
            print("Player 2 win")
    else:
        print("Invalid move")

    choice = input("Do you want to continue (Y/N)?").upper().strip()
    if choice == "N":
        break
