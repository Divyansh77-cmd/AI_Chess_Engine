# ♟️ Flask-Chess: A Minimax-Powered Chess Engine

A full-stack chess application built with a Flask-based Python backend and a reactive JavaScript frontend. This project features a custom-built chess engine powered by game theory algorithms to evaluate positions and select optimal moves.

---

## 🔬 How the Engine Thinks

The engine uses a multi-layered approach to analyze positions and make decisions.

### 1. Search Strategy

* **Minimax Algorithm**
  The core decision-making process. It assumes the opponent will always play the best possible move and selects moves that minimize maximum loss.

* **Alpha-Beta Pruning**
  An optimization technique that eliminates unnecessary branches in the search tree, allowing deeper searches in the same time.

* **Quiescence Search**
  Extends evaluation beyond depth limits during tactical positions (like captures) to avoid the *horizon effect*.

---

### 2. Position Evaluation

The engine evaluates positions using:

* **Material Values**
  Assigns numerical values to pieces (e.g., Pawn = 100, Queen = 900).

* **Piece-Square Tables (PST)**
  Provides positional bonuses based on piece placement (e.g., knights in the center are stronger).

* **Dynamic King Logic**

  * Opening/Middlegame: King safety is prioritized (corner positions rewarded)
  * Endgame: King activity is rewarded (central positions preferred)

---

### 3. Move Ordering

* **MVV-LVA (Most Valuable Victim - Least Valuable Aggressor)**
  Orders moves so that high-impact captures are evaluated first, improving pruning efficiency.

---

## 🛠️ Installation & Setup

### Prerequisites

* Python 3.10+
* pip (Python package manager)

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-chess-engine.git
cd flask-chess-engine
```

---

### 2. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install flask python-chess
```

---

## 🚀 Execution

Run the Flask server:

```bash
python app.py
```

Open your browser and go to:

👉 [http://localhost:5000](http://localhost:5000)

---

## 🕹️ Interface & Controls

* **Move Input:** Use Standard Algebraic Notation (SAN)

  * Examples: `e4`, `Nf3`, `O-O`, `exd5`

* **Visual Feedback:**

  * Engine move → dark green highlight
  * Player move → light green highlight

* **Move History:**

  * Displayed in a scrollable panel

* **Engine Status:**

  * Shows *"Thinking..."* during computation

---

## 📂 Project Structure

```
├── app.py              # Flask server & Chess Engine logic
├── templates/
│   └── index.html      # Frontend (optional external file)
└── README.md           # Project documentation
```

---

## 🔑 Key Functions (app.py)

| Function    | Purpose                                 |
| ----------- | --------------------------------------- |
| `minimax()` | Recursive search for best move          |
| `quiesce()` | Handles tactical positions beyond depth |
| `score()`   | Evaluates board position                |
| `move()`    | Flask route handling UI requests        |

---

## 📈 Future Enhancements

* Opening Book for faster early-game moves
* Transposition Tables to cache evaluated positions
* Web Workers for smoother UI performance

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author

**Divyansh Agarwal**
CSE Core, VIT Bhopal University (2025–2029)

---

> Built as part of a Digital Literacy / Full-Stack Development learning project 🚀
