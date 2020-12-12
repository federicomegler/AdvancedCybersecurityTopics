from pwn import *

flag = "flag{packer_asul_coolg+6$defghij}"
r = process(['john', flag])

gdb.attach(r, """b *0x0804922b
""")


