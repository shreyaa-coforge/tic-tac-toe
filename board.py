EMPTY = " "

class Board:
    '''A square Tic-Tac-Toe board.'''

    def __init__(self, size=3):
        if size < 3:
            raise ValueError("Board size must be at least 3")
        self._size = size
        self._grid = [[EMPTY for _ in range(size)] for _ in range(size)]

    @property
    def size(self):
        return self._size

    def cell(self, row, col):
        return self._grid[row][col]

    def _in_range(self, row, col):
        return 0 <= row < self._size and 0 <= col < self._size

    def place_mark(self, row, col, mark):
        '''Put mark at row, col. Return True if placed, False if taken or off-board.'''
        if not self._in_range(row, col):
            return False
        if self._grid[row][col] != EMPTY:
            return False
        self._grid[row][col] = mark
        return True

    def remove_mark(self, row, col):
        '''Remove a mark from row, col (used for minimax simulation).'''
        if self._in_range(row, col):
            self._grid[row][col] = EMPTY

    def empty_cells(self):
        '''Return a list of (row, col) tuples for every empty cell.'''
        return [(r, c) for r in range(self._size) for c in range(self._size) if self._grid[r][c] == EMPTY]

    def has_won(self, mark):
        '''Return True if mark fills a whole row, column, or diagonal.'''
        size = self._size
        # Check rows
        for row in self._grid:
            if all(cell == mark for cell in row):
                return True
        # Check columns
        for col in range(size):
            if all(self._grid[row][col] == mark for row in range(size)):
                return True
        # Check main diagonal
        if all(self._grid[i][i] == mark for i in range(size)):
            return True
        # Check other diagonal
        if all(self._grid[i][size - 1 - i] == mark for i in range(size)):
            return True
        return False

    def is_full(self):
        '''Return True if no empty cells remain.'''
        return len(self.empty_cells()) == 0

    def copy(self):
        '''Return an independent deep copy of this board for AI simulation.'''
        clone = Board(self._size)
        clone._grid = [row[:] for row in self._grid]  # Independent row slicing
        return clone

    def __str__(self):
        separator = "-" * (self._size * 4 - 1)
        lines = []
        for i, row in enumerate(self._grid):
            lines.append(" | ".join(row))
            if i < self._size - 1:
                lines.append(separator)
        return "\n".join(lines)