#!/usr/bin/python 


class MessageWriter(object):

     def __init__(self,file_name):

         self.file_name=file_name

     def __enter__(self):
         self.file=open(self.file_name,"w")
         return self.file

     def __exit__(self):
        self.file.close()


with MessageWriter('my_file.txt') as xfile: 
    xfile.write('hello world') 

