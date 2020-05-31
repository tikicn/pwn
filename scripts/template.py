from pwn import *

context(os="linux", arch="i386")
context.log_level = "debug"

HOST = "target"
PORT = 8080
conn = NotImplemented

if len(sys.argv) > 1 and sys.argv[2] == "r":
    conn = remote(HOST, PORT)
else:
    conn = process("./binary")
