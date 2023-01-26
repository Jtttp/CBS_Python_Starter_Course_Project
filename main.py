from entertaiment import *
from game import game
from art import *


tprint('welcome'.center(50, ' '))
tprint("to the entertainment bot", font="cybermedum")


def main():
    tprint('Let\'s start'.center(25, ' '), font='cybermedum')
    tq()

    while True:
        print('\nMenu:\n\n1. Read a joke\n2. Read an interesting fact\n3. Watch a movie\n'
              '4. Watch a TV series\n5. Listen music\n6. Play game\n'
              '\n0. Exit\n')
        choice = str(input('What will you choose? '))
        match choice:
            case '1':
                joke()
            case '2':
                fact()
            case '3':
                movie()
            case '4':
                series()
            case '5':
                music()
            case '6':
                game()
            case '0':
                tprint('Thank you! See you soon'.center(25, ' '), font='cybermedum')
                break
            case _:
                print('Incorrect. Let\'s try one more time!\n')


if __name__ == '__main__':
    main()
