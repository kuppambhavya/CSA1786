import numpy as np

WIN = 1
TIE = 0
LOSE = -1

board = np.array([['O', 'X', 'O'],
                  ['X', ' ', 'X'],
                  [' ', 'O', ' ']])

def minimax(board, maximizing_player, depth=0):
    """
    The Minimax function that returns the best move and the utility value
    of a terminal node.
    """
    result = check_game_result(board)
    if result is not None:
        return (None, result)

    if maximizing_player:
        player = 'O'
        best_value = LOSE
    else:
        player = 'X'
        best_value = WIN

    best_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = player
                _, value = minimax(board, not maximizing_player, depth + 1)
                board[row][col] = ' '
                if maximizing_player:
                    if value > best_value:
                        best_value = value
                        best_move = (row, col)
                else:
                    if value < best_value:
                        best_value = value
                        best_move = (row, col)

    return (best_move, best_value)

def check_game_result(board):
    """
    Function that returns the utility value of a terminal node.
    """
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            if board[row][0] == 'X':
                return LOSE
            else:
                return WIN

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            if board[0][col] == 'X':
                return LOSE
            else:
                return WIN

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        if board[0][0] == 'X':
            return LOSE
        else:
            return WIN

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        if board[0][2] == 'X':
            return LOSE
        else:
            return WIN

    if np.all(board != ' '):
        return TIE

    return None

best_move, best_value = minimax(board, True)

print("Best move:", best_move)
print("Utility value:", best_value)

if best_value >0:
    print("x wins")
else:
    print("o wins")
