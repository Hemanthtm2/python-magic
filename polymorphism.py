#!/usr/bin/python 

class Animal():

     def __init__(self,name):
         self.name=name

     def speak():
         return NotImplementedError("Subclass must implement this abstract method")

class Horse(Animal):

      def speak(self):
          return self.name + " says woof!"

h=Horse("Jackey")

print(h.speak())

