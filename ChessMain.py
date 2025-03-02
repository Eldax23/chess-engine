"""
this file will be responsible for handling input and gamestate.
"""

import pygame as p
import ChessEngine

p.init()

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

"""
Initialize a global dic of images
"""


def load_board():
    pieces = ["bB" , "bK" , "bN" , "bP" , "bQ" , "bR" , "wB" , "wK" , "wN" , "wP" , "wQ" , "wR"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load(f"Images/{piece}.png") , (SQ_SIZE , SQ_SIZE))



# this will handle user input and update graphics..


def main():
    p.init()
    screen = p.display.set_mode((WIDTH , HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    load_board()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        draw_game_state(screen , gs)
        clock.tick(MAX_FPS)
        p.display.flip()



# Handles all the graphical sides of the chess board
def draw_game_state(screen , gs):
    draw_board(screen)
    draw_pieces(screen , gs.board)


# Draw Squares
def draw_board(screen):
    colors = [p.Color("dark gray") , p.Color("dark green")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2 == 0]
            p.draw.rect(screen , color , (r * SQ_SIZE , c * SQ_SIZE , SQ_SIZE , SQ_SIZE))


# Draw the pieces
def draw_pieces(screen , board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece_name = board[r][c]
            if piece_name != "--":
                screen.blit(IMAGES[piece_name] , (SQ_SIZE * c , SQ_SIZE * r , SQ_SIZE , SQ_SIZE))





main()
