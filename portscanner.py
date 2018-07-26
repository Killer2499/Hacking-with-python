import socket
import os
import sys
from colorama import Fore, Back, Style
from datetime import datetime


#Clears the screen
os.system('clear')

print (Fore.GREEN+"-"*30+"Port Scanner"+"-"*30)
print ""
#Ask for input
server=raw_input("Enter a host name or IP address to scan:")
server_Ip=socket.gethostbyname(server)
print server_Ip

print "-" * 40
print "Starting Port Scanner!!!",server
print "-" * 40

#Time at which scan started
t1=datetime.now()

try:
	
	#Default is set to 1024 ports
	for port in range(0,1024):
		
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		
		result=sock.connect_ex((server_Ip,port))
		if result == 0 :
			print (Fore.RED+"Port %s: Open"%port)
			sock.close()

except KeyboardInterrupt:
	print "Exiting!!!"
	sys.exit()

except socket.gaierror():
	print "Hostname could not be resolved.Exiting!!"
	sys.exit()

except socket.error():
	print "Couldn't connect to server"
	sys.exit()

t2=datetime.now()
#Time at end of Scan

dur=t2-t1
#Total time taken to scan

print (Fore.GREEN+"Scanning Completed in : %s"%dur)
