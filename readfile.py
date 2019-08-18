#!/usr/bin/python 

myfile=open('test.txt')
print(myfile.read())

#curser adjustment to return the string
myfile.seek(0)

contents=myfile.read()

print(contents)
