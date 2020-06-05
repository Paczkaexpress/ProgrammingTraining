"""
Tic Tac Toe Player
"""

import math
from enum import Enum
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    xCounter = 0
    oCounter = 0

    for row in board:
        for x in row:
            if( x is "X"):
                xCounter += 1
            elif(x is "O"):
                oCounter += 1

    if(oCounter <= xCounter):
        return "O"
    else:
        return "X"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleMoves = list()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if(board[row][col] == None):
                possibleMoves.append((row, col))

    return possibleMoves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print(board)
    print(action)
    board[action[0]][action[1]] = player(board) 

    return board

def unresult(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = None

    return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = utility(board)
    if(winner == 1):
        return 'X'
    elif(winner == -1):
        return 'O'
    else:
        None
    
def terminal(board) -> bool:
    """
    Returns True if game is over, False otherwise.
    """
    
    counter = 0
    winner = utility(board)

    if(winner == 0):
        for row in board:    
            for x in row:
                if (x is "X" or x is 'O'):
                    counter += 1

        if (counter == 9):
            return True
        else:
            return False
    else:
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if((board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X') or
    (board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X') or 
    (board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X') or
    (board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X') or
    (board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X') or
    (board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X') or
    (board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X') or
    (board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X')):
        return 1
    elif((board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O') or
    (board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O') or 
    (board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O') or
    (board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O') or
    (board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O') or
    (board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O') or
    (board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O') or
    (board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O')):
        return -1
    else:
        return 0
        
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    p = player(board)

    if(p == 'X'):
        isMaxPlayer = True
    elif(p == 'O'):
        isMaxPlayer = False

    brdCopy = copy.deepcopy(board)
    bestMove = (0,0)

    def findBestMove_minmax(brdCopy, isMaxPlayer):
        bestMove = (0,0)
        m = (0,0)
        # print("Best move {}".format(bestMove))
        if terminal(brdCopy):
            return utility(brdCopy), (0,0)

        if isMaxPlayer:
            bestVal = -999
            for move in actions(brdCopy):
                brdCopy[move[0]][move[1]] = 'X'
                value, m = findBestMove_minmax(brdCopy, False)
                brdCopy[move[0]][move[1]] = None
                if(bestVal <= value):
                    bestVal = value
                    bestMove = move
            return bestVal, bestMove
        # print("Best move {}".format(bestMove))
        if isMaxPlayer == False:
            bestVal = 999
            for move in actions(brdCopy):
                brdCopy[move[0]][move[1]] = 'O'
                value, m = findBestMove_minmax(brdCopy, True)
                brdCopy[move[0]][move[1]] = None
                if(bestVal >= value):
                    bestVal = value
                    bestMove = move
            # print(bestVal)  
            return bestVal, bestMove

        # print("Best move {}".format(bestMove))
        return bestVal, bestMove

    val, bestMove = findBestMove_minmax(brdCopy, isMaxPlayer)
    print("Best move {}".format(bestMove))
    return bestMove