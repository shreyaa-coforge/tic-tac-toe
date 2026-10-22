import pytest
from board import Board

@pytest.fixture
def board():
    return Board(3)

def test_new_board_is_empty(board):
    assert len(board.empty_cells()) == 9
    assert board.is_full() is False

def test_place_mark_succeeds(board):
    assert board.place_mark(0, 0, "X") is True
    assert board.cell(0, 0) == "X"
    assert len(board.empty_cells()) == 8

def test_cannot_place_on_taken_cell(board):
    board.place_mark(0, 0, "X")
    assert board.place_mark(0, 0, "O") is False
    assert board.cell(0, 0) == "X"  # First mark stays intact

@pytest.mark.parametrize("row, col", [(-1, 0), (0, -1), (3, 0), (0, 3), (5, 5)])
def test_off_board_moves_are_rejected(board, row, col):
    assert board.place_mark(row, col, "X") is False
    assert len(board.empty_cells()) == 9

def test_win_across_row(board):
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    board.place_mark(0, 2, "X")
    assert board.has_won("X") is True
    assert board.has_won("O") is False

def test_win_down_column(board):
    board.place_mark(0, 1, "O")
    board.place_mark(1, 1, "O")
    board.place_mark(2, 1, "O")
    assert board.has_won("O") is True

def test_win_diagonal(board):
    board.place_mark(0, 0, "X")
    board.place_mark(1, 1, "X")
    board.place_mark(2, 2, "X")
    assert board.has_won("X") is True

def test_board_draw(board):
    # Fill board without a winner
    moves = [
        (0,0,"X"), (0,1,"O"), (0,2,"X"),
        (1,0,"X"), (1,1,"O"), (1,2,"O"),
        (2,0,"O"), (2,1,"X"), (2,2,"X")
    ]
    for r, c, m in moves:
        board.place_mark(r, c, m)
    
    assert board.is_full() is True
    assert board.has_won("X") is False
    assert board.has_won("O") is False