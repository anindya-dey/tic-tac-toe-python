def has_same_marker(board, positions, marker):
    for pos in positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == marker:
            return True

    return False


def has_player_won(board, player_marker):
    rows = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    columns = [ [1, 4, 7], [2, 5, 8], [3, 6, 9] ]
    diagonals = [ [1, 5, 9], [3, 5, 7] ]

    # Check rows
    if has_same_marker(board, rows, player_marker):
        return True
    
    # Check columns
    if has_same_marker(board, columns, player_marker):
        return True
    
    # Check diagonals
    if has_same_marker(board, diagonals, player_marker):
        return True

    return False
