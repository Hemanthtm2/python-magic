#!/usr/bin/python 


def player_input():

    marker=''
    while marker !='X' and marker !='O':
          marker=input("Player1,choose X or O: ")
          player1=marker 
          if player1=='X':
              player2='O'
          else:
             player2='X'
    return(player1,player2)
#    print(player1,player2)


player1_marker,player2_marker=player_input()

print("Player1 choose:",player1_marker)

print("Player2 choose:",player2_marker)


