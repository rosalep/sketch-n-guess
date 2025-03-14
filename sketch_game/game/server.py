import socket
import sys

# AF_NET = IPv4
# SOCK_STREAM = TCP
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# port = 8000

# try:
#     host_ip = socket.gethostbyname('localhost')
# except socket.gaierror:
#     print("Error in getting hostname")
#     sys.exit()

# s.connect((host_ip, port))
# print("socket connected")

s = socket.socket()         
print ("Socket successfully created")
 
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345               
 
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests 
# coming from other computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
 
# put the socket into listening mode 
s.listen(5)     
print ("socket is listening")            
 
# a forever loop until we interrupt it or 
# an error occurs 
while True: 
 
# Establish connection with client. 
  c, addr = s.accept()     
  print ('Got connection from', addr )
 
  # send a thank you message to the client. encoding to send byte type. 
  c.send('Thank you for connecting'.encode()) 
 
  # Close the connection with the client 
  c.close()
   
  # Breaking once connection closed
  break