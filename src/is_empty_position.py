def is_empty_position(board, pos):
    if str(board[pos]).isspace():
        return True
    
    return False