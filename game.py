from board import Board

class TicTacToeGame:
    def __init__(self, ai_opponent=None):
        self.board = Board(3)
        self.current_mark = "X"
        self.ai_opponent = ai_opponent
        self.ai_mark = "O" if ai_opponent else None
        self.game_over = False
        self.winner = None

    def play_turn(self, row, col):
        """Attempts to place the human player's mark."""
        if self.game_over:
            return False, "Game is already over."

        success = self.board.place_mark(row, col, self.current_mark)
        if not success:
            return False, "Invalid move! Cell is taken or out of bounds. Try again."

        if self._check_game_end_conditions():
            return True, self._get_end_message()

        # Switch turns
        self.current_mark = "O" if self.current_mark == "X" else "X"
        return True, "Move successful."

    def play_ai_turn(self):
        """Executes a move for the computer opponent using polymorphism."""
        if self.game_over or not self.ai_opponent or self.current_mark != self.ai_mark:
            return False, "Not AI's turn or no AI configured."

        # Polymorphic call: works for EasyAI or HardAI without knowing the subclass[cite: 27, 28]
        row, col = self.ai_opponent.choose_move(self.board, self.ai_mark)
        success = self.board.place_mark(row, col, self.ai_mark)
        
        if not success:
            return False, "AI attempted an invalid move."

        if self._check_game_end_conditions():
            return True, f"AI played at row {row+1}, col {col+1}. " + self._get_end_message()

        # Switch turn back to human
        self.current_mark = "X"
        return True, f"AI played at row {row+1}, col {col+1}."

    def _check_game_end_conditions(self):
        if self.board.has_won(self.current_mark):
            self.game_over = True
            self.winner = self.current_mark
            return True
        if self.board.is_full():
            self.game_over = True
            return True
        return False

    def _get_end_message(self):
        if self.winner:
            return f"Player {self.winner} wins!"
        return "It's a draw!"