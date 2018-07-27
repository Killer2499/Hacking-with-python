import socket

target_host="www.google.com"
target_port=80

#Create a socket object
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Connecting the client
client.connect((target_host,target_port))

#Sending data
client.send("GET/HTTP/1.1\r\nhost:google.com\r\n\r\n")

#Receiving response
response=client.recv(4096)

print response
