from os import system

"""
Guides user how to play every time app launches.
"""
class Tutorial:
    def __init__(self):
        is_on = True
        while is_on:
            system('cls')
            self.print_board()
            is_on = self.condition(self.tutorial_question())

    @staticmethod
    def print_board():
        print('\n\n 1 | 2 | 3')
        print('-' * 11)
        print(' 4 | 5 | 6')
        print('-' * 11)
        print(' 7 | 8 | 9')

    @staticmethod
    def condition(answer):
        if answer.lower() == 'y':
            return False
        return True

    @staticmethod
    def tutorial_question():
        question = input('\nEach field corresponds to number on your keyboard. Press 1-9 to enter X or O.\nType "y" to continue: ')
        return question
