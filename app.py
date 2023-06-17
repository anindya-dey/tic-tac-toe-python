from src.show_welcome_msg import show_welcome_msg
from src.choose_markers import choose_markers
from src.continue_game import continue_game
from src.clear_display import clear_display

def start_game():
    while True:
        clear_display()

        show_welcome_msg()

        markers = choose_markers()

        if not continue_game():
            break


start_game()