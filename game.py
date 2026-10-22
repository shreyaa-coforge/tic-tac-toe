from board import Board

class TicTacToeGame:
    def __init__(self):
        self.board = Board(3)
        self.current_mark = "X"
        self.game_over = False
        self.winner = None

    def play_turn(self, row, col):
        '''Attempts to place the current mark. Switches turn if successful.'''
        if self.game_over:
            return False, "Game is already over."

        success = self.board.place_mark(row, col, self.current_mark)
        if not success:
            return False, "Invalid move! Cell is taken or out of bounds. Try again."

        if self.board.has_won(self.current_mark):
            self.game_over = True
            self.winner = self.current_mark
            return True, f"Player {self.current_mark} wins!"

        if self.board.is_full():
            self.game_over = True
            return True, "It's a draw!"

        self.current_mark = "O" if self.current_mark == "X" else "X"
        return True, "Move successful."