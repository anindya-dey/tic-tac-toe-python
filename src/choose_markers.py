def choose_markers():
    while True:
        marker = input("Player 1, please choose a marker ('X' or 'O'): ").upper()

        if marker == 'X':
            return ('X', 'O')
        
        if marker == 'O':
            return ('O', 'X')

        print("Choose one out of 'X' or 'O'!")
