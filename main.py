from game import TicTacToeGame

def main():
    print("Welcome to Terminal Tic-Tac-Toe!")
    game = TicTacToeGame()

    while not game.game_over:
        print(f"\nCurrent Board (Player {game.current_mark}'s turn):")
        print(game.board)
        print("\nEnter your move as row and column numbered from 1 (e.g., 2 3):")

        user_input = input("Move > ").strip()
        parts = user_input.split()

        if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit():
            print("Invalid input! Please enter two numbers separated by a space (e.g., 2 3). Try again.")
            continue

        # Convert 1-indexed user input to 0-indexed coordinates
        row = int(parts[0]) - 1
        col = int(parts[1]) - 1

        success, message = game.play_turn(row, col)
        print(message)

    print("\nFinal Board State:")
    print(game.board)
    if game.winner:
        print(f"\nCongratulations! Player {game.winner} wins!")
    else:
        print("\nGame over! It's a draw.")

if __name__ == "__main__":
    main()