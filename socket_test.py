#!/usr/bin/python

import socket 


server=str(input("Enter the site you want to visit: \n"))

server_ip=socket.gethostbyname(server)

print(server_ip)
