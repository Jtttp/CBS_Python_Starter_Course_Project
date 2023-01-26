from art import *
from random import choice
from entertaiment import tq


def game():
    tq()
    tprint('\nGame Rock-Paper-Scissors'.center(25, ' '), font='cybermedum')
    print('\nRock, Paper or Scissors. What will you choose?')
    print('Press "0" for exit. Good luck!\n'.center(50, ' '))
    computer = 0
    player = 0

    while True:
        variant = ['rock', 'paper', 'scissors']
        computer_choice = choice(variant)
        player_choice = input('Your choice: ').lower().strip()
        print(f'Computer choose: {computer_choice}')
        if player_choice == '0':
            print(f'\nScore: \nComputer {computer} | Player {player}'.center(40, ' '))
            break
        if player_choice not in variant:
            print('\nIncorrect. Let\'s try one more time!\n')
        else:
            pass

            def define_winner(var1, var2):
                if var1 == var2:
                    return 'Draw'
                if var1 == 'rock':
                    return 'Computer' if var2 == 'paper' else 'Player'
                if var1 == 'paper':
                    return 'Computer' if var2 == 'scissors' else 'Player'
                if var1 == 'scissors':
                    return 'Computer' if var2 == 'rock' else 'Player'

            winner = define_winner(player_choice, computer_choice)
            if winner == 'Draw':
                print('Draw!'.center(40, ' '))
            elif winner == 'Player':
                print('You are the winner!'.center(40, ' '))
                player += 1
            else:
                print('Ohh! You lost!'.center(40, ' '))
                computer += 1

            print(f'Score: Computer {computer} | Player {player}\n')
