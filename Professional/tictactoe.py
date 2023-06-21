import random

# Tic Tac Toe

# Initialize the board
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")
        print("-------------")

# Function to check if the board is full
def is_board_full():
    return " " not in board

# Function to check if a player has won
def check_winner(player):
    # Check rows
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

# Function to make a move for the human player
def make_human_move():
    while True:
        position = input("Your turn. Choose a position (1-9): ")
        if not position.isdigit() or int(position) not in range(1, 10) or board[int(position) - 1] != " ":
            print("Invalid move. Please try again.")
            continue
        position = int(position) - 1
        board[position] = "X"
        break

# Function to make a move for the AI player
def make_ai_move():
    # Check for winning move
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "

    # Check for blocking move
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "

    # Make a random move
    while True:
        position = random.randint(0, 8)
        if board[position] == " ":
            board[position] = "O"
            return

# Function to play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        make_human_move()
        print_board()

        if check_winner("X"):
            print("You win!")
            break
        elif is_board_full():
            print("It's a tie!")
            break

        make_ai_move()
        print("AI's move:")
        print_board()

        if check_winner("O"):
            print("AI wins!")
            break
        elif is_board_full():
            print("It's a tie!")
            break

# Start the game
play_game()
