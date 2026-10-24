import random
import pytest
from board import Board
from ai import AIPlayer, EasyAI, HardAI

def test_abstract_ai_cannot_be_instantiated():
    """Verify abstract base class raises TypeError directly."""
    with pytest.raises(TypeError):
        AIPlayer()

def test_easy_ai_with_same_seed_makes_same_choice():
    """EasyAI with seeded random produces deterministic moves."""
    board = Board(3)
    ai1 = EasyAI(rng=random.Random(42))
    ai2 = EasyAI(rng=random.Random(42))
    assert ai1.choose_move(board, "O") == ai2.choose_move(board, "O")

def test_easy_ai_only_picks_empty_cells():
    """EasyAI never picks an occupied cell across multiple seed runs."""
    board = Board(3)
    board.place_mark(0, 0, "X")
    ai = EasyAI(rng=random.Random(123))
    for _ in range(20):
        move = ai.choose_move(board, "O")
        assert move in board.empty_cells()

def test_hard_ai_takes_winning_move():
    """HardAI immediately selects an available winning move."""
    board = Board(3)
    board.place_mark(0, 0, "O")
    board.place_mark(0, 1, "O")
    ai = HardAI()
    assert ai.choose_move(board, "O") == (0, 2)

def test_hard_ai_blocks_opponent_win():
    """HardAI blocks the human player from winning."""
    board = Board(3)
    board.place_mark(0, 0, "X")
    board.place_mark(0, 1, "X")
    ai = HardAI()
    assert ai.choose_move(board, "O") == (0, 2)

def test_choose_move_leaves_board_unchanged():
    """Ensure AI move selection does not permanently mutate board state during evaluation."""
    board = Board(3)
    board.place_mark(1, 1, "X")
    original_state = tuple(tuple(board.cell(r, c) for c in range(3)) for r in range(3))
    
    ai = HardAI()
    ai.choose_move(board, "O")
    
    after_state = tuple(tuple(board.cell(r, c) for c in range(3)) for r in range(3))
    assert after_state == original_state

def test_hard_ai_never_loses_as_second_player():
    """Explore every legal human choice against deterministic minimax AI."""
    ai = HardAI(rng=random.Random(42))
    seen = set()

    def explore(board, human_turn):
        state = (
            tuple(tuple(board.cell(r, c) for c in range(3)) for r in range(3)),
            human_turn,
        )
        if state in seen:
            return
        seen.add(state)

        assert not board.has_won("X"), "Human won against Hard AI"
        if board.has_won("O") or board.is_full():
            return

        if human_turn:
            for row, col in board.empty_cells():
                board.place_mark(row, col, "X")
                explore(board, False)
                board.remove_mark(row, col)
        else:
            before = state[0]
            row, col = ai.choose_move(board, "O")
            assert (row, col) in board.empty_cells()
            assert before == tuple(
                tuple(board.cell(r, c) for c in range(3)) for r in range(3)
            )
            board.place_mark(row, col, "O")
            explore(board, True)
            board.remove_mark(row, col)

    explore(Board(), True)
    assert len(seen) > 100
