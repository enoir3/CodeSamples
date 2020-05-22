# Spike fuzzer template originally used against Vulnserver located:
# https://github.com/stephenbradshaw/vulnserver
# In Kali, application-specific Spike templates are found in /usr/share/spike/audits
# 
# NOTE: multiple versions of the same spike are in this one file
# Find the one you want to use and delete the rest.
# Recommend you save the file as something else and not overwrite the original.
#!/usr/bin/perl

# Simple wrapper to run multiple .spk files using generic_send_tcp
$spikese = '/pentest/fuzzers/spike/generic_send_tcp';
if ($ARGV[4] eq '') {
	die("Usage: $0 IP_ADDRESS PORT SKIPFILE SKIPVAR SKIPSTR\n\n");
	}
$skipfiles = $ARGV[2];
@files = <*.spk>;
foreach $file (@files) {
	if (! $skipfiles) {
		if (system("$spikese $ARGV[0] $ARGV[1] $file $ARGV[3] $ARGV[4]") ) {
				print "Stopped processing file $file\n";
				exit(0);
				}
	} else {
		$skipfiles--;
	}
}

# The most basic fuzzer
s_readline(); // print received line from server
s_string_variable("COMMAND"); // send fuzzed string

# Slightly more complicated fuzzer - the one I used against Vulnserver
printf(“<COMMAND> ##<COMMAND>.spk : “); // print the command and filename to the terminal
s_readline(); // print the line received from the server
s_string(“<COMMAND> “); // send <COMMAND> to the application
s_string_variable(“COMMAND”); // send the fuzzed string to the application

# Fuzzer template that includes HTTP request header construction
# Add additional s_string variables to complete a custom HTTP header
# Nominal output for the code in this block:
# POST /testme.php HTTP/1.1
# Host: testserver.example.com
# Content-Length: [size_of_data]
# Connection: close
# inputvar=[fuzz_string]
s_string("POST /testme.php HTTP/1.1\r\n");
s_string("Host: testserver.example.com\r\n");
s_string("Content-Length: ");
s_blocksize_string("block1", 5);
s_string("\r\nConnection: close\r\n\r\n");
s_block_start("block1");
s_string("inputvar=");
s_string_variable("inputval");
s_block_end("block1");
