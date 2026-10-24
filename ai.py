import random
from abc import ABC, abstractmethod

class AIPlayer(ABC):
    """Base class for every computer opponent."""

    @abstractmethod
    def choose_move(self, board, mark):
        """Return a (row, col) tuple for an empty cell on the board."""
        pass

class EasyAI(AIPlayer):
    """Picks any empty cell at random using a seeded or default random generator."""

    def __init__(self, rng=None):
        if rng is None:
            rng = random.Random()
        self._rng = rng

    def choose_move(self, board, mark):
        empty = board.empty_cells()
        if not empty:
            raise ValueError("No empty cells available.")
        return self._rng.choice(empty)

class HardAI(AIPlayer):
    """Uses the minimax algorithm to play perfectly on a 3x3 board."""

    def __init__(self, rng=None):
        # Preserve the supplied generator for a consistent AI interface.
        # Minimax breaks equal-scoring ties deterministically.
        self._rng = rng if rng is not None else random.Random()

    def choose_move(self, board, mark):
        opponent = "O" if mark == "X" else "X"
        best_score = -float('inf')
        best_move = None

        for (row, col) in board.empty_cells():
            board.place_mark(row, col, mark)
            score = self._minimax(board, 0, False, mark, opponent)
            board.remove_mark(row, col)

            if score > best_score:
                best_score = score
                best_move = (row, col)

        return best_move

    def _minimax(self, board, depth, is_maximizing, ai_mark, human_mark):
        if board.has_won(ai_mark):
            return 10 - depth
        if board.has_won(human_mark):
            return depth - 10
        if board.is_full():
            return 0

        if is_maximizing:
            max_eval = -float('inf')
            for (row, col) in board.empty_cells():
                board.place_mark(row, col, ai_mark)
                eval = self._minimax(board, depth + 1, False, ai_mark, human_mark)
                board.remove_mark(row, col)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for (row, col) in board.empty_cells():
                board.place_mark(row, col, human_mark)
                eval = self._minimax(board, depth + 1, True, ai_mark, human_mark)
                board.remove_mark(row, col)
                min_eval = min(min_eval, eval)
            return min_eval