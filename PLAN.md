# PROJECT PLAN

## GOAL

This is a Tic-Tac-Toe game in Python that runs on Terminal. It allows the player to play against another human or against a computer as opponent locally. It gives two AI difficulty modes (Easy and Hard) and uses OOP architecture with tests.

## REQUIREMENTS

| ID | Requirement | Verification Method |
|---|---|---|
| 1 | The board is a 3 X 3 grid where 'X' always moves first. | Unit test in `tests/test_board.py` verifies new board state. |
| 2 | Invalid moves (taken cells, out-of-bounds coordinates, non-numeric input) are rejected without losing turn. | Unit tests in `tests/test_board.py` checking `place_mark` return values and CLI error handling. |
| 3 | The game correctly detects horizontal, vertical, and diagonal wins, as well as full-board draws. | Comprehensive win and draw test suite in `tests/test_board.py`. |
| 4 | `EasyAI` selects a random available cell on the board using a seeded `random.Random` instance. | Test in `tests/test_ai.py` verifying move validity and deterministic output with seeded RNG. |
| 5 | `HardAI` uses the minimax algorithm and never loses on a 3x3 board when playing second. | Exhaustive test exploring every legal human choice against deterministic `HardAI` in `tests/test_ai.py`. |
| 6 | Board state is encapsulated (`_grid`), and UI interaction (`print`/`input`) is isolated to `main.py`. | Source inspection verifies that only `main.py` uses terminal input/output and that `Board` stores its grid in `_grid`. |

## 3. Components

* **`board.py` (`Board` class):** Encapsulates grid state management, move validation, cell placement, win detection, and draw condition checks.
* **`ai.py` (`AIPlayer`, `EasyAI`, `HardAI` classes):** Defines the abstract base class and concrete AI strategies (`EasyAI` for random selection, `HardAI` using Minimax).
* **`game.py` (`TicTacToeGame` class):** Coordinates turn order, current player switching, move execution, and overall game status.
* **`main.py`:** Handles user interface interactions including menu prompts, CLI grid display, coordinate parsing, and main game execution loop.
* **`tests/`:** Contains unit test files validating grid logic, game rules, and AI behaviors using `pytest`.

## 4. Decisions

1. **AI Strategy Pattern via Abstract Base Class (`abc.ABC`)**
   * *Options Considered:* Functions with conditional statements (`if mode == 'easy'`) vs Object-Oriented Polymorphism via an ABC.
   * *Choice & Rationale:* Implemented `AIPlayer` as an abstract base class enforcing a `choose_move(board, mark)` contract. This decouples AI decision-making from game execution and makes adding future difficulty levels straightforward.

2. **Coordinate Parsing and Index Mapping in `main.py`**
   * *Options Considered:* Exposing 1-based coordinates throughout the domain model vs encapsulating 0-based indexing inside `Board` and converting user input exclusively in `main.py`.
   * *Choice & Rationale:* Handled conversion solely in `main.py` (subtracting 1 from user input). This keeps internal domain logic 0-indexed standard while providing an intuitive 1-indexed experience for humans.

---

## What Changed
- **Implementation Alignment:** The final implementation strictly followed the modular architecture outlined in the plan, separating concerns across `board.py`, `ai.py`, `game.py`, and `main.py`.
- **AI Polymorphism:** Utilized Python's `abc` module to establish an abstract `AIPlayer` interface, allowing `EasyAI` and `HardAI` to be swapped seamlessly into the game logic without conditional checking.
- **Testing Enhancements:** Added comprehensive parameterized `pytest` fixtures and seeded random generators to thoroughly validate edge cases, off-board inputs, win/draw states, and minimax optimality without relying on unseeded randomness or real time.
## Post-submission learning changes
- Added reverse-diagonal, turn-handling, and exhaustive second-player Hard AI tests.
- Compared full board state around AI move selection instead of only counting empty cells.
- Removed unused `Board.copy()` helper and stray citation markers.
- Added menu validation and made HardAI retain the injected RNG object (move ties remain deterministic).
- Corrected the README instructions and aligned the plan with actual tests.
