"""
print("   \n\n                WELCOME TO TEMU'S TIC TAC TOE GAME                ")
"""
import random

"""
draw the board ======TICK
create two players =======TICK
win functIon ==========TICK
IF YOU WRITE ON A TAKEN SPACE ERROR AND TRY AGAIN ========TICK
MAKE THE PLAYER PLAY WITH THE COMPUTER =================

"""
tic_toe = ['-', '-', '-', '-', '-', '-', '-', '-', '-']


def interface():
    # global display
    print(' 1'' |' ' 2  ' '|' ' 3 ''\n'' 4 ''|' ' 5  ' '|' ' 6 ''\n' ' 7'' |' ' 8  ' '|'' 9 ' '\n')

    way_to_play = int(
        input('HOW WOULD YOU LIKE TO PLAY:-\n (1) TO PLAY WITH A FRIEND :-- \n (2) PLAY WITH A COMPUTER :--  '))

    if way_to_play == 1:
        player_one()
        player_two()

    elif way_to_play == 2:
        def display():
            for j in range(0, 9):
                print('check one two three')
                print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[j], tic_toe[j], tic_toe[j]))
                print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[j], tic_toe[j], tic_toe[j]))
                print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[j], tic_toe[j], tic_toe[j]))
                random.choices(tic_toe[j])
                str(tic_toe[j]) == 'O'
                display()
                j += 1
                human()

        def human():
            for i in range(0, 10):
                user_choice = int(input('HUMAN ON WHICH SPACE DO YOU WANT TO WRITE: '))

                def show():
                    print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[0], tic_toe[1], tic_toe[2]))
                    print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[3], tic_toe[4], tic_toe[5]))
                    print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[6], tic_toe[7], tic_toe[8]))

                if user_choice == 1:
                    if tic_toe[0] == 'X' or tic_toe[0] == 'O':
                        print('space taken:- please try again')

                    tic_toe[0] = 'X'

                elif user_choice == 2:
                    if tic_toe[1] == 'X' or tic_toe[1] == 'O':
                        print('space taken:- please try again')

                    tic_toe[1] = 'X'

                elif user_choice == 3:
                    if tic_toe[2] == 'X' or tic_toe[2] == 'O':
                        print('space taken:- please try again')

                    tic_toe[2] = 'X'

                elif user_choice == 4:
                    if tic_toe[3] == 'X' or tic_toe[3] == 'O':
                        print('space taken:- please try again')

                    tic_toe[3] = 'X'

                elif user_choice == 5:
                    if tic_toe[4] == 'X' or tic_toe[4] == 'O':
                        print('space taken:- please try again')

                    tic_toe[4] = 'X'

                elif user_choice == 6:
                    if tic_toe[5] == 'X' or tic_toe[5] == 'O':
                        print('space taken:- please try again')

                    tic_toe[5] = 'X'

                elif user_choice == 7:
                    if tic_toe[6] == 'X' or tic_toe[6] == 'O':
                        print('space taken:- please try again')

                    tic_toe[6] = 'X'

                elif user_choice == 8:
                    if tic_toe[7] == 'X' or tic_toe[7] == 'O':
                        print('space taken:- please try again')

                    tic_toe[7] = 'X'

                elif user_choice == 9:
                    if tic_toe[8] == 'X' or tic_toe[8] == 'O':
                        print('space taken:- please try again')

                    tic_toe[8] = 'X'

                else:
                    print('INVALID CHOICE!')

                display()


def player_one():
    for i in range(0, 10):
        user_choice = int(input('PLAYER ONE ON WHICH SPACE DO YOU WANT TO WRITE: '))

        def show():
            print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[0], tic_toe[1], tic_toe[2]))
            print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[3], tic_toe[4], tic_toe[5]))
            print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[6], tic_toe[7], tic_toe[8]))

        if user_choice == 1:
            if tic_toe[0] == 'X' or tic_toe[0] == 'O':
                print('space taken:- please try again')

            tic_toe[0] = 'X'

        elif user_choice == 2:
            if tic_toe[1] == 'X' or tic_toe[1] == 'O':
                print('space taken:- please try again')

            tic_toe[1] = 'X'

        elif user_choice == 3:
            if tic_toe[2] == 'X' or tic_toe[2] == 'O':
                print('space taken:- please try again')

            tic_toe[2] = 'X'

        elif user_choice == 4:
            if tic_toe[3] == 'X' or tic_toe[3] == 'O':
                print('space taken:- please try again')

            tic_toe[3] = 'X'

        elif user_choice == 5:
            if tic_toe[4] == 'X' or tic_toe[4] == 'O':
                print('space taken:- please try again')

            tic_toe[4] = 'X'

        elif user_choice == 6:
            if tic_toe[5] == 'X' or tic_toe[5] == 'O':
                print('space taken:- please try again')

            tic_toe[5] = 'X'

        elif user_choice == 7:
            if tic_toe[6] == 'X' or tic_toe[6] == 'O':
                print('space taken:- please try again')

            tic_toe[6] = 'X'

        elif user_choice == 8:
            if tic_toe[7] == 'X' or tic_toe[7] == 'O':
                print('space taken:- please try again')

            tic_toe[7] = 'X'

        elif user_choice == 9:
            if tic_toe[8] == 'X' or tic_toe[8] == 'O':
                print('space taken:- please try again')

            tic_toe[8] = 'X'

        else:
            print('INVALID CHOICE!')

        wining_func()
        show()
        player_two()
        print('next move')


def player_two():
    for i in range(0, 10):
        user2_choice = user_choice = int(input('PLAYER TWO ON WHICH SPACE DO YOU WANT TO WRITE: '))

        def show():
            print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[0], tic_toe[1], tic_toe[2]))
            print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[3], tic_toe[4], tic_toe[5]))
            print('\t\t\t'' {} '  ' | '   ' {}   ''| '   ' {} '.format(tic_toe[6], tic_toe[7], tic_toe[8]))

        if user2_choice == 1:
            if tic_toe[0] == 'X' or tic_toe[0] == 'O':
                print('space taken:- please try again')

            tic_toe[0] = 'O'

        elif user2_choice == 2:
            if tic_toe[1] == 'X' or tic_toe[1] == 'O':
                print('space taken:- please try again')

            tic_toe[1] = 'O'

        elif user2_choice == 3:
            if tic_toe[2] == 'X' or tic_toe[2] == 'O':
                print('space taken:- please try again')

            tic_toe[2] = 'O'

        elif user2_choice == 4:
            if tic_toe[3] == 'X' or tic_toe[3] == 'O':
                print('space taken:- please try again')

            tic_toe[3] = 'O'

        elif user2_choice == 5:
            if tic_toe[4] == 'X' or tic_toe[4] == 'O':
                print('space taken:- please try again')

            tic_toe[4] = 'O'

        elif user2_choice == 6:
            if tic_toe[5] == 'X' or tic_toe[5] == 'O':
                print('space taken:- please try again')

            tic_toe[5] = 'O'

        elif user2_choice == 7:
            if tic_toe[6] == 'X' or tic_toe[6] == 'O':
                print('space taken:- please try again')

            tic_toe[6] = 'O'

        elif user2_choice == 8:
            if tic_toe[7] == 'X' or tic_toe[7] == 'O':
                print('space taken:- please try again')

            tic_toe[7] = 'O'

        elif user2_choice == 9:
            if tic_toe[8] == 'X' or tic_toe[8] == 'O':
                print('space taken:- please try again')

            tic_toe[8] = 'O'

        else:
            print('INVALID CHOICE!')

        show()
        wining_func()
        player_one()
        print('next move')


def wining_func():
    if (str(tic_toe[0]) == str(tic_toe[1]) == str(tic_toe[2])) == 'X' or (str(tic_toe[0]) == str(tic_toe[1]) == str(
            tic_toe[2])) == 'O':
        if (str(tic_toe[0]) == str(tic_toe[1]) == str(tic_toe[2])) == 'X':
            print('player one won ')
        elif (str(tic_toe[0]) == str(tic_toe[1]) == str(tic_toe[2])) == 'O':
            print('player two won')
        exit(0)
    elif (str(tic_toe[3]) == str(tic_toe[4]) == str(tic_toe[5])) == 'X' or (str(tic_toe[3]) == str(tic_toe[4]) == str(
            tic_toe[5])) == 'O':
        if (str(tic_toe[3]) == str(tic_toe[4]) == str(tic_toe[5])) == 'X':
            print('player one won ')
        elif (str(tic_toe[3]) == str(tic_toe[4]) == str(tic_toe[5])) == 'O':
            print('player two won')
        exit(0)
    elif (str(tic_toe[6]) == str(tic_toe[7]) == str(tic_toe[8])) == 'X' or (str(tic_toe[6]) == str(tic_toe[7]) == str(
            tic_toe[8])) == 'O':
        if (str(tic_toe[6]) == str(tic_toe[7]) == str(tic_toe[8])) == 'X':
            print('player one won ')
        elif (str(tic_toe[6]) == str(tic_toe[7]) == str(tic_toe[8])) == 'O':
            print('player two won')
        exit(0)
    elif (str(tic_toe[0]) == str(tic_toe[3]) == str(tic_toe[6])) == 'X' or (str(tic_toe[0]) == str(tic_toe[3]) == str(
            tic_toe[6])) == 'O':
        if (str(tic_toe[0]) == str(tic_toe[3]) == str(tic_toe[6])) == 'X':
            print('player one won ')
        elif (str(tic_toe[0]) == str(tic_toe[3]) == str(tic_toe[6])) == 'O':
            print('player two won')
        exit(0)
    elif (str(tic_toe[1]) == str(tic_toe[4]) == str(tic_toe[7])) == 'X' or (str(tic_toe[1]) == str(tic_toe[4]) == str(
            tic_toe[7])) == 'O':
        if (str(tic_toe[1]) == str(tic_toe[4]) == str(tic_toe[7])) == 'X':
            print('player one won ')
        elif (str(tic_toe[1]) == str(tic_toe[4]) == str(tic_toe[7])) == 'O':
            print('player two won')
        exit(0)
    elif (str(tic_toe[2]) == str(tic_toe[5]) == str(tic_toe[8])) == 'X' or (str(tic_toe[2]) == str(tic_toe[5]) == str(
            tic_toe[8])) == 'O':
        if (str(tic_toe[2]) == str(tic_toe[5]) == str(tic_toe[8])) == 'X':
            print('player one won ')
        elif (str(tic_toe[2]) == str(tic_toe[5]) == str(tic_toe[8])) == 'O':
            print('player two won')
        exit(0)
    elif (str(tic_toe[0]) == str(tic_toe[4]) == str(tic_toe[8])) == 'X' or (str(tic_toe[0]) == str(tic_toe[4]) == str(
            tic_toe[8])) == 'O':
        if (str(tic_toe[0]) == str(tic_toe[4]) == str(tic_toe[8])) == 'X':
            print('player one won ')
        elif (str(tic_toe[0]) == str(tic_toe[4]) == str(tic_toe[8])) == 'O':
            print('player two won')
        exit(0)
    elif (str(tic_toe[2]) == str(tic_toe[4]) == str(tic_toe[6])) == 'X' or (str(tic_toe[2]) == str(tic_toe[4])) == str(
            tic_toe[6]) == 'O':
        if (str(tic_toe[2]) == str(tic_toe[4]) == str(tic_toe[6])) == 'X':
            print('player one won ')
        elif (str(tic_toe[2]) == str(tic_toe[4]) == str(tic_toe[6])) == 'O':
            print('player two won')
        exit(0)


interface()
