def print_board(board):
    """Prints the Tic Tac Toe board in a nice format."""
    print()
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print()


def check_winner(board, player):
    """Checks if the given player has won."""
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in win_combinations)


def tic_tac_toe():
    board = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    taken = []
    current_player = "X"

    print("🎮 Welcome to Tic Tac Toe!")
    print("Game starts with X")
    print_board(board)

    for turn in range(9):
        while True:
            move = input(f"{current_player}'s turn. Choose a block (a-i): ").lower()

            if move not in board:
                print("❌ Invalid input! Choose from a to i.")
            elif move in taken:
                print("⚠️ That spot is already taken!")
            else:
                break

        index = board.index(move)
        board[index] = current_player
        taken.append(move)

        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 {current_player} wins!")
            break

        current_player = "O" if current_player == "X" else "X"
    else:
        print("🤝 It's a draw!")

    # Option to play again
    again = input("Play again? (y/n): ").lower()
    if again == "y":
        tic_tac_toe()


# Start the game
tic_tac_toe()
