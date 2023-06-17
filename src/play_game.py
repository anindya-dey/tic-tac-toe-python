from src.display_board import display_board
from src.place_marker import place_marker

def play_game(markers):
    board = [' '] * 10

    display_board(board)

    place_marker(board, markers)

    #while True:


