# Global Variables
board = [' '] * 10
game_state = True
announce = ''

def reset_board():
    global board, game_state
    board = [' '] * 10
    game_state = True

def display_board():
    print("  " + board[7] + " | " + board[8] + " | " + board[9])
    print("------------")
    print("  " + board[4] + " | " + board[5] + " | " + board[6])
    print("------------")
    print("  " + board[1] + " | " + board[2] + " | " + board[3])

def win_check(board, player):
    return ((board[7] == board[8] == board[9] == player) or
            (board[4] == board[5] == board[6] == player) or
            (board[1] == board[2] == board[3] == player) or
            (board[7] == board[4] == board[1] == player) or
            (board[8] == board[5] == board[2] == player) or
            (board[9] == board[6] == board[3] == player) or
            (board[1] == board[5] == board[9] == player) or
            (board[3] == board[5] == board[7] == player))

def full_board_check(board):
    return not " " in board[1:]

def ask_player(mark):
    global board
    req = f'Choose where to place your {mark} (1-9): '
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print("Sorry, please input a number between 1-9.")
            continue

        if choice not in range(1, 10):
            print("Sorry, please input a number between 1-9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print("That space isn't empty!")

def player_choice(mark):
    global board, game_state, announce
    announce = ''
    ask_player(mark)

    if win_check(board, mark):
        display_board()
        announce = mark + " wins! Congratulations"
        game_state = False
    else:
        display_board()

    if full_board_check(board):
        announce = "Tie!"
        game_state = False

    return game_state, announce

def play_game():
    reset_board()
    global announce

    X = 'X'
    O = 'O'

    while True:
        display_board()
        game_state, announce = player_choice(X)
        print(announce)
        if not game_state:
            break

        game_state, announce = player_choice(O)
        print(announce)
        if not game_state:
            break

    rematch = input('Would you like to play again? y/n: ')
    if rematch.lower() == 'y':
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
play_game()

