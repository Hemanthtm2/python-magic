#!/usr/bin/python

def master_yoda(text):
    new_string=""
    new_list=text.split()
    new_list=new_list[::-1]
    new_string=new_string+' '.join(new_list)
    return new_string

result=master_yoda('We are Ready')

print(result)
