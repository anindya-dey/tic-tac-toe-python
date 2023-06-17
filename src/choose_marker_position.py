from src.is_empty_position import is_empty_position

def choose_marker_position(board, current_marker):
    while True:
        try:
            pos = int(input(f"Please select a number between 1 and 9 to place marker '{current_marker}': "))

            if pos not in range(1, 10) or not is_empty_position(board, pos):
                print("Please select a valid number between 1 and 9!")
            else:
                return pos
        except:
            print("Please select a valid number between 1 and 9!")
