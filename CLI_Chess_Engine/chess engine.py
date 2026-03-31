import chess
import math
import sys

PIECE_VALUES = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

UNICODE_PIECES = {
    'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
    'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚'
}

RESET = "\033[0m"
WHITE_BG = "\033[47m"
BLACK_BG = "\033[100m"
WHITE_PIECE = "\033[97m"
BLACK_PIECE = "\033[30m"

def evaluate(board):
    if board.is_checkmate():
        return -99999 if board.turn else 99999

    score = 0
    for piece_type in PIECE_VALUES:
        score += len(board.pieces(piece_type, chess.WHITE)) * PIECE_VALUES[piece_type]
        score -= len(board.pieces(piece_type, chess.BLACK)) * PIECE_VALUES[piece_type]

    return score


def quiescence(board, alpha, beta):
    stand_pat = evaluate(board)

    if stand_pat >= beta:
        return beta
    if alpha < stand_pat:
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiescence(board, -beta, -alpha)
            board.pop()

            if score >= beta:
                return beta
            if score > alpha:
                alpha = score

    return alpha


def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0 or board.is_game_over():
        return quiescence(board, alpha, beta)

    if maximizing:
        max_eval = -math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, False)
            board.pop()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, alpha, beta, True)
            board.pop()
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def get_best_move(board, depth):
    best_move = None
    best_value = -math.inf

    for move in board.legal_moves:
        board.push(move)
        value = minimax(board, depth - 1, -math.inf, math.inf, False)
        board.pop()

        if value > best_value:
            best_value = value
            best_move = move

    return best_move


def print_board(board):
    print("\n    a   b   c   d   e   f   g   h")
    print("  +---+---+---+---+---+---+---+---+")

    for rank in range(7, -1, -1):
        row = f"{rank+1} |"
        for file in range(8):
            square = chess.square(file, rank)
            piece = board.piece_at(square)

            bg = WHITE_BG if (rank + file) % 2 == 0 else BLACK_BG

            if piece:
                symbol = UNICODE_PIECES[piece.symbol()]
                color = WHITE_PIECE if piece.color == chess.WHITE else BLACK_PIECE
                cell = f"{bg}{color} {symbol} {RESET}"
            else:
                cell = f"{bg}   {RESET}"

            row += cell + "|"

        print(row + f" {rank+1}")
        print("  +---+---+---+---+---+---+---+---+")

    print("    a   b   c   d   e   f   g   h\n")


def print_help():
    print("""
Commands:
  e4, Nf3, O-O  -> Make a move (SAN)
  undo          -> Undo last move
  restart       -> Restart game
  help          -> Show help
  exit          -> Quit
""")


def play():
    board = chess.Board()

    print("♟️ CLI Chess Engine")
    print_help()

    try:
        depth = int(input("Select difficulty (1-4): "))
    except:
        depth = 3

    move_stack = []

    while True:
        print_board(board)

        if board.is_game_over():
            print("Game Over! Result:", board.result())
            break

        user_input = input("Your move: ").strip()

        if user_input == "exit":
            print("Goodbye!")
            sys.exit()

        elif user_input == "help":
            print_help()
            continue

        elif user_input == "undo":
            if len(move_stack) >= 2:
                board.pop()
                board.pop()
                move_stack.pop()
                move_stack.pop()
            else:
                print("Nothing to undo!")
            continue

        elif user_input == "restart":
            board.reset()
            move_stack.clear()
            print("Game restarted!")
            continue

        try:
            move = board.parse_san(user_input)
            board.push(move)
            move_stack.append(move)
        except:
            print("Invalid move. Try again.")
            continue

        if board.is_game_over():
            continue

        print("Engine thinking...")
        engine_move = get_best_move(board, depth)

        move_san = board.san(engine_move)
        board.push(engine_move)
        move_stack.append(engine_move)

        print(f"Engine plays: {move_san}")


if __name__ == "__main__":
    play()