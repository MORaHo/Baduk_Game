### Variables
### I'm putting them here to help clean the file up

## Board Varibles

BLACK = 1
WHITE = 2
block = []
pre_board = [] #board before stone placement
liberties = []
post_board = [] #board after stone placement and capture
black_moves = []
white_moves = []
seki_counter = 0
pre_pre_board = [] #
current_player = BLACK
opposing_player = WHITE 
size_without_offset = 13
moves = [[],black_moves,white_moves]
SIZE = size_without_offset + 2

## Pygame Variables

run            = True
space          = 40
width          = (SIZE-1) * space #size considers both offboards, 
height         = (SIZE-1) * space
white          = (255,255,255)
black          = (0,0,0)
beige          = (171,144,88)
LINE_COLOUR    = (0,0,0) 
COLOUR_ARRAY   = [0,black,white]
PLAYER_ARRAY   = [0,BLACK,WHITE]
current_colour = black
