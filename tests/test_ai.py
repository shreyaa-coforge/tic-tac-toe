import random
import pytest
from board import Board
from ai import AIPlayer, EasyAI, HardAI

def test_abstract_ai_cannot_be_instantiated():
    """Verify abstract base class raises TypeError directly[cite: 27, 84]."""
    with pytest.raises(TypeError):
        AIPlayer()

def test_easy_ai_with_same_seed_makes_same_choice():
    """EasyAI with seeded random produces deterministic moves[cite: 28, 82]."""
    board = Board(3)
    ai1 = EasyAI(rng=random.Random(42))
    ai2 = EasyAI(rng=random.Random(42))
    assert ai1.choose_move(board, "O") == ai2.choose_move(board, "O")

def test_easy_ai_only_picks_empty_cells():
    """EasyAI never picks an occupied cell across multiple seed runs[cite: 82]."""
    board = Board(3)
    board.place_mark(0, 0, "X")
    ai = EasyAI(rng=random.Random(123))
    for _ in range(20):
        move = ai.choose_move(board, "O")
        assert move in board.empty_cells()

def test_hard_ai_takes_winning_move():
    """HardAI immediately selects an available winning move[cite: 9]."""
    board = Board(3)
    board.place_mark(0, 0, "O")
    board.place_mark(0, 1, "O")
    ai = HardAI()
    assert ai.choose_move(board, "O") == (0, 2)

def test_hard_ai_blocks_opponent_win():
    """HardAI blocks the human player from winning[cite: 9]."""
    board = Board(3)
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    ai = HardAI()
    assert ai.choose_move(board, "O") == (0, 2)

def test_choose_move_leaves_board_unchanged():
    """Ensure AI move selection does not permanently mutate board state during evaluation[cite: 9, 18]."""
    board = Board(3)
    board.place_mark(1, 1, "X")
    original_empty_count = len(board.empty_cells())
    
    ai = HardAI()
    ai.choose_move(board, "O")
    
    assert len(board.empty_cells()) == original_empty_count