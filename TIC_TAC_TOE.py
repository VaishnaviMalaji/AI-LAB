# Tic-Tac-Toe using Minimax Algorithm

MAX = 'O'   # Computer
MIN = 'X'   # Human


# Check whether a player has won
def check_winner(board, player):
    # Rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True

    # Columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True

    # Diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


# TERMINAL-TEST(state)
def terminal_test(board):
    if check_winner(board, MAX):
        return True

    if check_winner(board, MIN):
        return True

    # Check for draw
    for row in board:
        for cell in row:
            if cell == '_':
                return False

    return True


# UTILITY(state)
def utility(board):
    if check_winner(board, MAX):
        return 1

    if check_winner(board, MIN):
        return -1

    return 0


# ACTIONS(state)
def actions(board):
    moves = []

    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                moves.append((i, j))

    return moves


# RESULT(state, action)
def result(board, action, player):
    new_board = [row[:] for row in board]

    i, j = action
    new_board[i][j] = player

    return new_board


# MAX-VALUE(state)
def max_value(board):
    if terminal_test(board):
        return utility(board)

    v = float('-inf')

    for action in actions(board):
        new_board = result(board, action, MAX)
        v = max(v, min_value(new_board))

    return v


# MIN-VALUE(state)
def min_value(board):
    if terminal_test(board):
        return utility(board)

    v = float('inf')

    for action in actions(board):
        new_board = result(board, action, MIN)
        v = min(v, max_value(new_board))

    return v


# MINIMAX-DECISION(state)
def minimax_decision(board):
    best_action = None
    best_value = float('-inf')

    for action in actions(board):
        new_board = result(board, action, MAX)
        value = min_value(new_board)

        if value > best_value:
            best_value = value
            best_action = action

    return best_action


# Display board
def print_board(board):
    for row in board:
        print(' '.join(row))


# Main program
def play_tictactoe(board):
    print("Input board:")
    print_board(board)

    # If computer can make a move
    if not terminal_test(board):
        move = minimax_decision(board)

        row, col = move

        board[row][col] = MAX

        print()
        print("Computer places O in position", (row + 1, col + 1))

        print_board(board)

    # Check result
    if check_winner(board, MAX):
        print("Computer Wins")

    elif check_winner(board, MIN):
        print("Human Wins")

    else:
        print("Game Draw")


# --------------------------------------------------
# TEST CASE 1
# --------------------------------------------------

board1 = [
    ['O', 'O', '_'],
    ['X', 'X', '_'],
    ['_', '_', '_']
]

print("TEST CASE 1")
play_tictactoe(board1)


# --------------------------------------------------
# TEST CASE 2
# --------------------------------------------------

board2 = [
    ['X', 'X', '_'],
    ['O', '_', '_'],
    ['_', '_', '_']
]

print()
print("TEST CASE 2")
play_tictactoe(board2)


# --------------------------------------------------
# TEST CASE 3
# --------------------------------------------------

board3 = [
    ['X', 'O', 'X'],
    ['X', 'O', 'O'],
    ['O', 'X', '_']
]

print()
print("TEST CASE 3")
play_tictactoe(board3)