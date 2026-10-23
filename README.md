# Tic-Tac-Toe with AI Opponent

A robust, object-oriented command-line Tic-Tac-Toe game written in Python 3. It supports a two-player mode (Human vs. Human) and a single-player mode against a computer opponent with **Easy** (random) and **Hard** (Minimax) difficulty levels.

## Features
- **Strict Separation of Concerns:** Game rules, board logic, and AI strategies are completely decoupled from terminal input/output (`print()` / `input()`)[cite: 36].
- **Object-Oriented Design:** Encapsulated `Board` state with a read-only size property, and an abstract base class (`AIPlayer`) implemented using Python's `abc` module[cite: 18, 27].
- **Minimax AI:** `HardAI` utilizes the minimax algorithm and never loses when playing second on a 3x3 board[cite: 9, 28].
- **Test-Driven Development:** Comprehensive test coverage via `pytest` with seeded randomness and parameterized tests[cite: 76, 81, 82].
- **Automated CI Pipeline:** GitHub Actions continuous integration workflow verifying automated tests on every push and pull request[cite: 42].

---

## How to Run the Game

1. **Clone the repository and navigate to the project root:**
   ```bash
   git clone <your-repository-url>
   cd tic-tac-toe

2. **Set up and activate your virtual environment:**
    python3 -m venv venv
    source venv/bin/activate
3. **Install dependencies:**
    pip install -r requirements.txt
4. **Launch the game:**
    python3 main.py

**How to Play:**
Choose your game mode from the startup menu (Two Players, Easy AI, or Hard AI).
Enter your moves as row and column numbers separated by a space (e.g., 2 3), indexed from 1[cite: 10].

**How to Run the Tests**
Make sure your virtual environment is active, then run pytest:   
    pytest -v