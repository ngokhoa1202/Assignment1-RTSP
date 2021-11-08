
# Import socket module
import socket            
 
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)        
 
# Define the port on which you want to connect
port = 4010
 
# connect to the server on local computer
while True: 
    msg = 'concac'
    s.sendto(msg.encode("utf-8"),('', port))
 
# receive data from the server and decoding to get the string.
# print (s.recv(1024).decode())
# close the connection
s.close()   