from pwn import *

conn=process('ropasaurusrex')

conn.sendline('A'*140)
print(conn.recvline())