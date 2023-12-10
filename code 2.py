import math

# Constants for representing the players and empty cells
X = 'X'
O = 'O'
EMPTY = ' '

# Function to print the board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---------')

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all(board[i][j] != EMPTY for i in range(3) for j in range(3))

# Function to get available moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, maximizing_player):
    if check_winner(board, X):
        return 1
    elif check_winner(board, O):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i, j in get_available_moves(board):
            board[i][j] = X
            eval = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for i, j in get_available_moves(board):
            board[i][j] = O
            eval = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

# Function to find the best move using minimax
def get_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i, j in get_available_moves(board):
        board[i][j] = X
        eval = minimax(board, 0, False)
        board[i][j] = EMPTY
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
    return best_move

# Function to play Tic-Tac-Toe
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe! You are playing as 'O'.")
    print_board(board)

    while True:
        # Player's move
        while True:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if (row, col) in get_available_moves(board):
                board[row][col] = O
                break
            else:
                print("Invalid move! Try again.")

        # Check if player wins or board is full
        if check_winner(board, O):
            print("Congratulations! You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # AI's move
        row, col = get_best_move(board)
        board[row][col] = X
        print("\nAI's move:")
        print_board(board)

        # Check if AI wins or board is full
        if check_winner(board, X):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

# Start the game
play_game()
