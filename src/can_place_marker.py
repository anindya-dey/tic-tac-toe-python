from src.is_empty_position import is_empty_position

def can_place_marker(board, position, marker):
    if is_empty_position(board, position):
        board[position] = marker
        return True
    
    print(f"Marker '{marker}' can not be placed at position '{position}', Try again!")
    return False
