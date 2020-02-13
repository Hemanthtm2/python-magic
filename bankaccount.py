#!/usr/bin/python 


class Account():

     def __init__(self,owner,balance):
         self.owner=owner 
         self.balance=balance 

     def __str__(self):

        return f" Account name is: {self.owner} \n Account balance; {self.balance}"


     def deposit(self,dep_amt):
         return f"Your account balance is {self.balance+dep_amt}"




     def withdraw(self,wd_amt):
          if wd_amt <= self.balance:
             self.balance=self.balance-wd_amt
             return f"You have with drawn {wd_amt} and your current balance is {self.balance}"
          else:
              return "You do not have suffient balance to procced with this transaction"
         


a=Account("HEMANTH",1000)

print(a)

#print(a.deposit(10))

print(a.withdraw(100))
