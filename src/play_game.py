from src.display_board import display_board
from src.choose_marker_position import choose_marker_position
from src.clear_display import clear_display
from src.has_player_won import has_player_won
from src.can_place_marker import can_place_marker


def play_game(markers):
    board = [' '] * 10

    display_board(board)

    current_player = 0

    while True:
        current_marker = markers[current_player]

        pos = choose_marker_position(board, current_marker)

        if has_player_won(board, current_marker):
            print(f"Player {current_player+1} has won!")
            break

        if not can_marker_placed(board, pos, current_marker):
            print("it's a tie!")
            break

        clear_display()

        display_board(board)

        current_player ^= 1 # Toggle between 0 and 1 to switch between player turns

    #while True:
