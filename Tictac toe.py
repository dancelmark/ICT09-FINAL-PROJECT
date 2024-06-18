def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board, mark):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    return [mark, mark, mark] in win_conditions


def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player1 = input("Enter name for player 1: ")
    player2 = input("Enter name for player 2: ")
    players = [(player1, "X"), (player2, "O")]
    current_player = 0

    for turn in range(9):
        print_board(board)
        player_name, mark = players[current_player]
        print(f"{player_name}'s turn. You are '{mark}'")
        while True:
            try:
                row, col = map(int, input("Enter row and column (0, 1, or 2): ").split())
                if board[row][col] == " ":
                    board[row][col] = mark
                    break
                else:
                    print("Cell already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter numbers between 0 and 2 separated by space.")

        if check_winner(board, mark):
            print_board(board)
            print(f"Congratulations {player_name}! You win!")
            return
        current_player = 1 - current_player

    print_board(board)
    print("It's a tie!")


tic_tac_toe()
