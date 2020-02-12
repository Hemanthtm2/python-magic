#!/usr/bin/python 

class Animal():

     def __init__(self,name):
         self.name=name 

     def speak(self):
         return self.name + " Says woof"

class Dog(Animal):
     
      def __init__(self,name):
          Animal.__init__(self,name)

mydog=Dog("buckey")

print(mydog.speak())
