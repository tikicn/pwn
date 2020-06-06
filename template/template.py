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

# elf=ELF(FILE_NAME)
# addr_main=elf.symbols["main"]
# addr_bss=elf.bss()
# addr_dynsym=elf.get_section_by_name(".dynsym").header["sh_addr"]
#
# libc=ELF("./")
# libc_sh=nex(libc.search(b"/bin/sh"))


def main():
    conn.interactive()


if __name__ == "__main__":
    main()
