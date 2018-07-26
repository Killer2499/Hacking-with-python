import hashlib #Different types of hashing
import crypt #For cryptographic hashes
#import secrets  generating cryptographically strong random numbers
#python 3.6
import random
from colorama import Fore, Back, Style


print (Fore.RED +"-----------En-De cypter-------------")


print (Fore.GREEN+"Select :")
print "1.Paswword Hashing"
print "2.Password Decrypting"

option=raw_input("Select Option:")

print(Style.RESET_ALL)
print 'Select hashing method:'
print "0.Default"
print "1.md5"
print "2.crypt(Only Encrypting)"
print "3.sha1"
print "4.sha224"
print "5.sha256"
print "6.sha384"
print "7.sha512"

select = raw_input("Select type:")
method='0'

def hash(select,method):
	if select == '1':
		method = 'md5'
	elif select == '2':
		pass
	elif select == '3':
		method = 'sha1'					
	elif select == '4':
		method = 'sha224'	
	elif select == '5':
		method = 'sha256'	
	elif select == '6':
		method = 'sha384'
	elif select == '7':
		method = 'sha512'
	elif select == '0':
		method = 'md5'
	else:
		select = raw_input("Select hashing method1111:")
		select_hash(select,method)
	return method

method1=hash(select,method)
	



if option == '1':
	
 	print (method1)

	
	print (Fore.GREEN +"Password Hasher!!!")
	passwd_hash = raw_input("Enter your password:")
	
	if select == '2':
		print "Salt type:"
		print "a.Random"
		print "b.Enter Salt"
		salt_type = raw_input("Enter salt type:")
		
		if salt_type == 'a':
			salt=str(random.choice([hex(x) for x in xrange(0,pow(2, 16))]))
		else:	
			salt=raw_input("Enter salt value:")
			
		crypt_hash=crypt.crypt(passwd_hash,salt)
		print "Your hashed passwd is:%s"%crypt_hash
	else: 	
		hash1=getattr(hashlib,method1)(passwd_hash)
		print "Your hashed passwd is : ",hash1.hexdigest()


if option == '2':
 	
	print (Fore.GREEN+"-----------Password Decrypter---------")
	hashed_passwd =raw_input("Enter your hashed password:")

	#wordlist=raw_input("Enter wordlist file:")
	wordlist='bruteforce.txt'
	try:
	    wordlist=open(wordlist,'r')
	    wordlist=wordlist.read()
	    wordlist=wordlist.split()
	except:
	    print "\n!!!Wordlist not found!!!"
	    quit()

	for password in wordlist:

		hashed=getattr(hashlib,method1)(password)
		
		if hashed_passwd == hashed.hexdigest():
			print "Password Found!!!: %s"%password
			break
		else :  
			print (Fore.RED+"[*]Decrpyting")
			
			
