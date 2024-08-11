import numpy 

#global variables
EMPTY = 0
BLACK = 1
WHITE = 2
MARKER = 4
OFFBOARD = 7
LIBERTY = 8

def score(board,komi):
    
    black_score = komi
    white_score = 0

    return black_score, white_score

