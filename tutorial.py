
"""
Guides user how to play every time app launches.
"""

# shows 'GUI' to the user
def tutorial():
    while True:
        print('\n\n 1 | 2 | 3')
        print('-' * 11)
        print(' 4 | 5 | 6')
        print('-' * 11)
        print(' 7 | 8 | 9')

        user_tutorial_question = input('\nEach field corresponds to number on your keyboard. '
                                       'Press 1-9 to enter X or O.\nType "y" to continue: ')
        if user_tutorial_question.lower() == 'y':
            break
        else:
            continue
