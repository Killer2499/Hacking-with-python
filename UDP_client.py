import socket

target_host="127.0.0.1"
target_port=80

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.sendto("AASDAS",(target_host,target_port))

data,addr=client.recvfrom(4096)

print data

print addr
#Hostname and port 

