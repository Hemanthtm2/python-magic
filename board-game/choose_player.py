#!/usr/bin/python 

import random
def choose_first():

    flip=random.randint(0,1)
    if flip==0:
       return 'Player1'
    else:
      return 'Player2'


print(choose_first())
