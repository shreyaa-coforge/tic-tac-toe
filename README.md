# Tic-Tac-Toe with AI Opponent

A terminal-based Python 3 Tic-Tac-Toe game with two-player mode, random Easy AI, and minimax Hard AI.

## Requirements

Python 3.10 or later.

## Run locally

Create and activate a virtual environment:

```bash
python -m venv .venv
```

 `source .venv/bin/activate`

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the game:

```bash
python main.py
```

Enter a mode of 1 (two players), 2 (easy computer), or 3 (hard computer). Moves are row and column numbers from 1 to 3, e.g. `2 3`. Invalid moves do not use up a turn.

## Run tests

```bash
python -m pytest -v
```

Tests cover the board, invalid turn handling, seeded Easy AI, Hard AI decision-making, state preservation, and an exhaustive game-tree check that the Hard AI does not lose when playing second.

## Architecture

- `board.py`: grid state and rules
- `ai.py`: abstract AI interface, EasyAI, HardAI with minimax
- `game.py`: turns and game outcomes
- `main.py`: terminal input/output
- `tests/`: pytest tests
