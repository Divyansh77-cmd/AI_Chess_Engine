# ♟️ CLI Chess Engine (Minimax AI)

This project is a **Command Line Interface (CLI) based Chess Engine** built in Python. It allows a user to play chess directly in the terminal against an AI powered by the **Minimax algorithm with Alpha-Beta pruning**.

The application is fully terminal-based and does not require any graphical interface.

---

## 🚀 Features

* Play chess in the terminal
* AI opponent using Minimax algorithm
* Alpha-Beta pruning for efficiency
* Quiescence search for better move evaluation
* Colored chess board with Unicode pieces
* Adjustable difficulty levels
* Undo and restart functionality

---

## 🧰 Prerequisites

Make sure you have the following installed on your system:

* **Python 3.10 or higher**
* **pip (Python package manager)**

To check Python version:

```bash
python --version
```

---

## ⚙️ Installation & Setup

Follow these steps carefully to set up the project.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cli-chess-engine.git
cd cli-chess-engine
```

---

### 2. Create a Virtual Environment (Recommended)

#### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install python-chess
```

---

## ▶️ Running the Application

Run the following command in your terminal:

```bash
python chess_engine.py
```

---

## 🎮 How to Play

* The chessboard will appear in the terminal
* You play as **White**, and the AI plays as **Black**
* Enter moves using **Standard Algebraic Notation (SAN)**

### Examples:

* `e4` → Move pawn
* `Nf3` → Move knight
* `O-O` → Castle kingside
* `exd5` → Capture move

---

## 🕹️ Commands

| Command | Description       |
| ------- | ----------------- |
| e4, Nf3 | Make a move       |
| undo    | Undo last move    |
| restart | Restart the game  |
| help    | Show command list |
| exit    | Quit the game     |

---

## 🎯 Difficulty Levels

At the start of the game, you will be prompted to choose a difficulty level:

* `1` → Easy (fast, shallow search)
* `2-3` → Medium (balanced)
* `4+` → Hard (slower but stronger AI)

---

## 🧠 How the AI Works

The chess engine uses the following techniques:

* **Minimax Algorithm**: Simulates future moves assuming optimal play
* **Alpha-Beta Pruning**: Skips unnecessary branches to improve speed
* **Quiescence Search**: Handles tactical positions beyond depth limit
* **Evaluation Function**: Scores positions based on material balance

---

## 📁 Project Structure

```
.
├── chess_engine.py   # Main CLI application and engine logic
└── README.md         # Project documentation
```

---

## ⚠️ Notes

* Ensure your terminal supports ANSI colors for best experience
* Works best in:

  * Windows Terminal / PowerShell
  * VS Code Terminal
  * Linux / macOS terminals

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Divyansh Agarwal**
CSE Core, VIT Bhopal University (2025–2029)

---

> This project demonstrates implementation of game theory and AI algorithms in a fully functional CLI-based application.
