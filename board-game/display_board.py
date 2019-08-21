#!/usr/bin/python 


def display_board(board):

    print("\n")
    print(board[6]+'|'+board[7]+'|'+board[8])
    print('-----')     
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----') 
    print(board[0]+'|'+board[1]+'|'+board[2])


test_board=[' ']*10

display_board(test_board)
