import optparse
import socket
from threading import *

screenLock=Semaphore(value=1)
scan=0
def connect_scan(tgthost,tgtport):
	
	try:
		sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((tgthost,tgtport))
		sock.send('Testing\r\n')
		results=sock.recv(100)
		print '[+]%d/tcp open' %tgtport 
		print '[+]' + str(results)
		
	
	except:
		screenLock.acquire()
		#print '[-]%d/tcp closed' %tgtport

	finally:
		screenLock.release()
		sock.close()
def port_scan(tgthost,tgtports):

	print '\n[+]Scan Results for: '+tgthost

	if tgtports == 0:
		for tgtport in range (0,1024):
			t=Thread(target=connect_scan,args=(tgthost,int(tgtport)))
			t.start()

	else:
		for tgtport in tgtports:
			t=Thread(target=connect_scan,args=(tgthost,int(tgtport)))
			t.start()
			


def main():
	parser=optparse.OptionParser('usage %prog -H <target_host> -p <target_port>')
	parser.add_option('-H', dest='tgthost', type='string', help='specify target host')
	parser.add_option('-p', dest ='tgtport', type='string', help='Specify tagert Port')

	(options,args) = parser.parse_args()

	tgthost=options.tgthost
	tgtports=str(options.tgtport).split(',')

	if (tgthost == None) :
		print "[-] You must specify a target host and port[s]"
		exit(0)

	if (tgthost != None) and (options.tgtport == None):
		tgtports=0

	port_scan(tgthost,tgtports)
main()
