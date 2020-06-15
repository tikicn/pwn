from pwn import *
import sys

# config
context(os="linux", arch="i386")
context.log_level = "debug"

FILE_NAME = ""
HOST = ""
PORT = 0

if len(sys.argv) > 1 and sys.argv[1] == "r":
    conn = remote(HOST, PORT)
else:
    conn = process(FILE_NAME)


# buflen=0
# elf=ELF(FILE_NAME)
# bss=elf.bss()
# printf_plt=elf.plt['printf']
# printf_got=elf.got['printf']
# main_addr=elf.symbols['main']


def main():

    payload = b"A"*buflen
    payload += p32(0x12345678)
    conn.sendlineafter(">", payload)
    conn.interactive()


if __name__ == "__main__":
    main()
