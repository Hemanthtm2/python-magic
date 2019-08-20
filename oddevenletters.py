#!/usr/bin/python

def myfunc(name='Hemanth'):
    mylist=[]
    for index in range (len(name)):
        if index % 2==0:
            mylist.append(name[index].upper())
        else:
            mylist.append(name[index].lower())
    return ''.join(mylist)

result=myfunc('Hemanth')
print(result)
