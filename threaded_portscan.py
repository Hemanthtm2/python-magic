#!/usr/bin/python 


import threading 
import time 
from queue import Queue

import socket

print_lock=threading.Lock()



target = 'hackthissite.org'

def portscan(port):

   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   try:
      s.connect(target,port)
      
      with print_lock:
           print('port',port)
      con.close()

   except:
        pass

def threader():
 
    while True:
          worker = q.get()
          portscan(worker)
          q.task_done()

q=Queue()




for x in range(30):
   t = threading.Thread(target=threader)
   t.daemon = True
   t.start()

start = time.time()


for worker in range(1,100):
    q.put(worker)


q.join()


