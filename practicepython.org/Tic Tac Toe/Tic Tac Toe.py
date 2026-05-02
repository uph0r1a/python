import os


def draw_board(board):
    size = len(board)
    for i in range(size):
        print(" ---" * size)
        for j in range(size):
            cell = board[i][j]
            symbol = " "
            if cell == 1:
                symbol = "X"
            elif cell == 2:
                symbol = "O"
            print(f"| {symbol} ", end="")
        print("|")
    print(" ---" * size)


def check_winner(board):
    size = len(board)

    for row in board:
        if row.count(row[0]) == size and row[0] != 0:
            return row[0]

    for col in range(size):
        column = [board[row][col] for row in range(size)]
        if column.count(column[0]) == size and column[0] != 0:
            return column[0]

    diag1 = [board[i][i] for i in range(size)]
    diag2 = [board[i][size - i - 1] for i in range(size)]

    if diag1.count(diag1[0]) == size and diag1[0] != 0:
        return diag1[0]

    if diag2.count(diag2[0]) == size and diag2[0] != 0:
        return diag2[0]

    return 0


def is_full(board):
    return all(cell != 0 for row in board for cell in row)


def get_move(player, size):
    while True:
        move = input(
            f"Player {player} ({'X' if player == 1 else 'O'}), enter move (row,col): "
        )
        try:
            row, col = map(int, move.split(","))
            row -= 1
            col -= 1

            if 0 <= row < size and 0 <= col < size:
                return row, col
            else:
                print("Out of bounds! Try again.")
        except:
            print("Invalid format! Use row,col (example: 1,3)")


def play_game():
    size = int(input("Enter board size (e.g. 3 for 3x3): "))
    board = [[0 for _ in range(size)] for _ in range(size)]

    current_player = 1

    while True:
        os.system("clear")
        draw_board(board)

        row, col = get_move(current_player, size)

        if board[row][col] != 0:
            print("That spot is already taken! Try again.")
            input("Press Enter to continue...")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            os.system("clear")
            draw_board(board)
            print(f"🎉 Player {winner} ({'X' if winner == 1 else 'O'}) wins!")
            break

        if is_full(board):
            os.system("clear")
            draw_board(board)
            print("It's a draw!")
            break

        current_player = 2 if current_player == 1 else 1


play_game()
