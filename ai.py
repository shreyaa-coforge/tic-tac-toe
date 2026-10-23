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