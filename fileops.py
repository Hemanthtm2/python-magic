#!/usr/bin/python 

##instaed of f.close() function we can use with statement ##

with open('my_new_file.txt',mode='r') as f:
     print(f.read())

with open('my_new_file.txt',mode='a') as f:
     f.write("This is thrid line")

with open('my_new_file.txt',mode='r') as f:
     print(f.read())

with open('mypython.txt',mode='w') as f:
     f.write('I created this file')

with open('mypython.txt',mode='r') as f:
     print(f.read())
