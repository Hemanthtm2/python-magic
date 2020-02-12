#!/usr/bin/python

class Dog():
      species="Mammal"
      def __init__(self,breed,name):
          self.breed=breed
          self.name=name

      def bark(self,number):
          print("WOOF...My name is {} and my number is {}".format(self.name,number))

mydog=Dog(breed="Lab",name="Frankie")


print(mydog.species)

print(mydog.bark(1))
