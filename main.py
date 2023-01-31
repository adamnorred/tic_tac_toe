import tutorial
from functions import *

# game value fields
FIELD_DICT = {'1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' ', '6': ' ', '7': ' ', '8': ' ', '9': ' '}

# winning combinations
WIN_ROWS = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


start_tutorial = tutorial.Tutorial()


# for restarting fresh game
while True:
    os.system('cls')
    FIELD_DICT = clear_dict_values(FIELD_DICT)  # reset all values stored in dict to start fresh game
    show_board(field_dict=FIELD_DICT)

    # main game loop
    while True:
        player_turn(player_num='1', player_char='X', field_dict=FIELD_DICT)
        if check_win(player_num='1', player_char='X', field_dict=FIELD_DICT, win_rows=WIN_ROWS):
            break
        if is_tie(field_dict=FIELD_DICT):
            break
        player_turn(player_num='2', player_char='O', field_dict=FIELD_DICT)
        if check_win(player_num='2', player_char='O', field_dict=FIELD_DICT, win_rows=WIN_ROWS):
            break
        if is_tie(field_dict=FIELD_DICT):
            break

    # check if user wants to play again
    if play_again():
        continue
    else:
        break
