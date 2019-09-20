# This script checks if the port is open. The socket module can be simply used to check if the port is open or not
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('irc.myserver.net', 6667))
if result == 0:
   print "Port is open"
else:
   print "Port is not open"
