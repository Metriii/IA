"""
Tic Tac Toe Player
"""

import copy
import math

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
    player_x = sum(row.count(X) for row in board)
    player_O = sum(row.count(O) for row in board)

    return O if player_x > player_O else X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    posicoes = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                posicoes.add((i,j))

    return posicoes


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError('jogada invalida')

    novo = copy.deepcopy(board)
    i , j = action
    novo[i][j] = player(board)
    return novo




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board [0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]

    if board [0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[1][1]

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or not actions(board)
        


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner (board) == O:
        return -1

    return 0
    


def minimax(board):
    if terminal(board):
        return None

    valor = lambda b: utility(b) if terminal(b) else (
        max(valor(result(b, a)) for a in actions(b))
        if player(b) == X
        else min(valor(result(b, a)) for a in actions(b))
    )

    jogador = player(board)
    melhor = None
    melhor_valor = -math.inf if jogador == X else math.inf

    for acao in sorted(actions(board)):
        v = valor(result(board, acao))
        if (jogador == X and v > melhor_valor) or (jogador == O and v < melhor_valor):
            melhor_valor = v
            melhor = acao

    return melhor

        

