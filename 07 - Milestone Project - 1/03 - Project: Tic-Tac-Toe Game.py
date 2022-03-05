
def display_board(board):
    print('\n'*100)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or # across top
            (board[4] == board[5] == board[6] == mark) or # across middle
            (board[1] == board[2] == board[3] == mark) or # across bottom
            (board[7] == board[4] == board[1] == mark) or # down left
            (board[8] == board[5] == board[2] == mark) or # down middle
            (board[9] == board[6] == board[3] == mark) or # down right
            (board[7] == board[5] == board[3] == mark) or # diagonal
            (board[9] == board[5] == board[1] == mark))   # diagonal


import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board): # boş kutu kaldı mı
    for i in range(1, 10):
        if space_check(board, i):
            return False # return sonrası aşağı devam etmez direk fonksiyondan çıkar
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose a position: (1-9) '))
    return position


def replay():
    choice = input('Play Again ? Enter Yes or No ')
    return choice == 'Yes'




# WHILE LOOP TO KEEP RUNNING THE GAME
print('Welcome to the TIC TAC TOE')

while True:

    ## SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,0)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play ? y or n? ').upper()
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    ## PLAY GAME

    while game_on:
        if turn == 'Player 1':

            # Show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player1_marker, position)

            # Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!!')
                game_on = False
            else:
                # Check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Show the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the position
            place_marker(the_board, player2_marker, position)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!!')
                game_on = False
            else:
                # Check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Tie game')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


