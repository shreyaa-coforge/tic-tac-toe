import random
from game import TicTacToeGame
from ai import EasyAI, HardAI

def main():
    print("Welcome to Terminal Tic-Tac-Toe!")
    print("\nSelect Game Mode:")
    print("1. Two Players (Human vs Human)")
    print("2. Versus Computer (Easy)")
    print("3. Versus Computer (Hard)")

    while True:
        mode_choice = input("Enter choice (1, 2, or 3): ").strip()
        if mode_choice in ("1", "2", "3"):
            break
        print("Invalid choice. Enter 1, 2, or 3.")
    
    ai_opponent = None
    if mode_choice == "2":
        ai_opponent = EasyAI(rng=random.Random())
        print("\nMode selected: Human (X) vs Easy Computer (O)")
    elif mode_choice == "3":
        ai_opponent = HardAI(rng=random.Random())
        print("\nMode selected: Human (X) vs Hard Computer (O)")
    else:
        print("\nMode selected: Two Players (X vs O)")

    game = TicTacToeGame(ai_opponent=ai_opponent)

    while not game.game_over:
        print(f"\nCurrent Board (Player {game.current_mark}'s turn):")
        print(game.board)

        # If it's the computer's turn, let the AI play automatically
        if game.ai_opponent and game.current_mark == game.ai_mark:
            print("\nComputer is thinking...")
            success, message = game.play_ai_turn()
            print(message)
            continue

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