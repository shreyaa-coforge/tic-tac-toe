from game import TicTacToeGame


def test_invalid_move_does_not_consume_turn():
    game = TicTacToeGame()
    assert game.play_turn(0, 0)[0] is True
    assert game.current_mark == "O"
    assert game.play_turn(0, 0)[0] is False
    assert game.current_mark == "O"
    assert game.play_turn(-1, 1)[0] is False
    assert game.current_mark == "O"


def test_alternating_turns_and_win():
    game = TicTacToeGame()
    for row, col in [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]:
        success, _ = game.play_turn(row, col)
        assert success
    assert game.game_over is True
    assert game.winner == "X"
    assert game.play_turn(2, 2)[0] is False
