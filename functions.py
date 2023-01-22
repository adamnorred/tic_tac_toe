import os

"""
All functions needed for game to work .
"""


# checks if user wants to play again
def play_again():
    while True:
        human_input = input('\nPlay again? (y/n): ').lower()
        if human_input != 'y' and human_input != 'n':
            print('Wrong input. Try again.')
            continue
        if human_input == 'y':
            return True
        else:
            return False


# clear game value fields from dictionary
def clear_dict_values(any_dict):
    any_dict = {key: ' ' for (key, value) in any_dict.items()}
    return any_dict


# checks if player has the right combination to win game
def check_win(player_num, player_char, field_dict, win_rows):
    for row in win_rows:
        if field_dict[str(row[0])] == player_char and field_dict[str(row[1])] == player_char and field_dict[str(row[2])] == player_char:
            print(f'\nPlayer {player_num}({player_char}) wins.')
            return True


# checks if all fields are full
def is_tie(field_dict):
    if ' ' not in field_dict.values():
        print('\nTie.')
        return True


# displays board
def show_board(field_dict):
    print(f'\n\n {field_dict["1"]} | {field_dict["2"]} | {field_dict["3"]}')
    print('-' * 11)
    print(f' {field_dict["4"]} | {field_dict["5"]} | {field_dict["6"]}')
    print('-' * 11)
    print(f' {field_dict["7"]} | {field_dict["8"]} | {field_dict["9"]}')


# let user input char 'X' or 'O', checks for wrong input or if field is taken
# if all conditions are checked, inserts char into right field
def player_turn(player_num, player_char, field_dict):
    while True:
        player_input = input(f'\nPlayer {player_num} turn({player_char}): ')
        if player_input not in field_dict.keys():
            print('Wrong input. Use 1-9 characters to choose field. Try again.')
            continue
        elif field_dict[f'{player_input}'] != ' ':
            print('Sorry, this field is taken. Try again.')
            continue
        else:
            field_dict[f'{player_input}'] = player_char
            os.system('cls')
            show_board(field_dict=field_dict)
            break
