﻿# https://codereview.stackexchange.com/questions/108738/python-tic-tac-toe-game
# http://inventwithpython.com/chapter10.html

# with random()

import random

def tic_tac_toe():
    board = [None] + list(range(1, 10))
    WIN_COMBINATIONS = [
       (1, 2, 3),
       (4, 5, 6),
       (7, 8, 9),
       (1, 4, 7),
       (2, 5, 8),
       (3, 6, 9),
       (1, 5, 9),
       (3, 5, 7),
    ]

    def draw():
        print(' ' , board[7] , ' | ' , board[8] , ' | ' , board[9])
        print('-----------------')
        print(' ' , board[4] , ' | ' , board[5] , ' | ' , board[6])
        print('-----------------')
        print(' ' , board[1] , ' | ' , board[2] , ' | ' , board[3])
        print()
    
    def choose_number():
        while True:
            try:
                a = int(input())
                if a in board:
                    return a
                #elif a == 0:
                #    break
                else:
                    print("\nInvalid move. Try again")
            except ValueError:
               print("\nThat's not a number. Try again")
               
    def choose_number_comp():
        while True:
            a = random.randint(1, 9)
            if a in board:
                return a

    def is_game_over():
        for a, b, c in WIN_COMBINATIONS:
            if board[a] == board[b] == board[c]:
                print("Player {0} wins!\n".format(board[a]))
                print("Congratulations!\n")
                return True
        if 9 == sum((pos == 'X' or pos == 'O') for pos in board):
            print("The game ends in a tie\n")
            return True

    for player in 'XO' * 9:    # для выбора за кого играть Х или О - менять местами ХО и ОХ
        draw()
        q = 0
        if is_game_over():
            break
        print("Player {0} pick your move".format(player))
        if q % 2 == 0:
            board[choose_number()] = player
        else: 
            board[choose_number_comp()] = player     # играет комп
        q += 1
        print()

while True:
    tic_tac_toe()
    if input("Play again (y/n)\n") != "y":
        break