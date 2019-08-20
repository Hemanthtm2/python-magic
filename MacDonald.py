#!/usr/bin/python 

def old_macdonald(name):
    new_name=""
    for i in range(0,len(name)):
        if i==0 or i==3:
           new_name=new_name+str(name[i].upper())
        else:
           new_name=new_name+name[i]
    return new_name
print(old_macdonald("macdonald"))
