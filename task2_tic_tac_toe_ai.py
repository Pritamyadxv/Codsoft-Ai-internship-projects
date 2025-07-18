# task2_tic_tac_toe_ai.py
# Tic Tac Toe Game with Basic AI for CodSoft Internship

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def ai_move(board):
    return random.choice(empty_cells(board))

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    print("Welcome to Tic Tac Toe! You are X, AI is O.")
    print_board(board)

    for turn in range(9):
        if turn % 2 == 0:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue
            board[row][col] = "X"
        else:
            row, col = ai_move(board)
            board[row][col] = "O"
            print(f"AI moved at ({row}, {col})")

        print_board(board)

        if check_win(board, "X"):
            print("You win!")
            return
        elif check_win(board, "O"):
            print("AI wins!")
            return

    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()
