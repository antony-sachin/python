import tkinter as tk
from tkinter import messagebox
import math

# Initialize the game board
board = [' ' for _ in range(9)]

# Check for winner
def check_winner(b, player):
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(b[i] == player for i in combo) for combo in win_combinations)

# Check for draw
def is_draw():
    return ' ' not in board

# Get all valid moves
def available_moves():
    return [i for i in range(9) if board[i] == ' ']

# Minimax Algorithm
def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'):
        return 1
    elif check_winner(b, 'X'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in available_moves():
            b[move] = 'O'
            score = minimax(b, depth + 1, False)
            b[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves():
            b[move] = 'X'
            score = minimax(b, depth + 1, True)
            b[move] = ' '
            best_score = min(score, best_score)
        return best_score

# Computer's move using Minimax
def computer_move():
    best_score = -math.inf
    best_move = None
    for i in available_moves():
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            best_move = i
    board[best_move] = 'O'
    buttons[best_move].config(text='O', state='disabled')
    check_game_over()

# Handle player's move
def on_button_click(index):
    if board[index] == ' ':
        board[index] = 'X'
        buttons[index].config(text='X', state='disabled')
        check_game_over()
        if not check_winner(board, 'X') and not is_draw():
            computer_move()

# Check game result
def check_game_over():
    if check_winner(board, 'X'):
        messagebox.showinfo("Game Over", "You Win! 🎉")
        reset_game()
    elif check_winner(board, 'O'):
        messagebox.showinfo("Game Over", "Computer Wins! 🤖")
        reset_game()
    elif is_draw():
        messagebox.showinfo("Game Over", "It's a Draw!")
        reset_game()

# Reset the game
def reset_game():
    global board
    board = [' ' for _ in range(9)]
    for button in buttons:
        button.config(text=' ', state='normal')

# Tkinter GUI setup
root = tk.Tk()
root.title("Tic-Tac-Toe - Minimax AI")

buttons = []
for i in range(9):
    btn = tk.Button(root, text=' ', font=('Arial', 24), height=2, width=5,
                    command=lambda i=i: on_button_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

root.mainloop()
