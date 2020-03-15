#!/usr/bin/python 

def func():

    print("func() in one.py")

print("Top level in one.py")


if __name__ == '__main__':
   print("ONE.py is being run directly")

else:
  print("one.py has been imported")
