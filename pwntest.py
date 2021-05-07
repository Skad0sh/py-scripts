from pwn import *
import re

context.log_level='debug'
io = remote('159.65.156.133',1337)
skip = 0

def decodeNsend(a):
    if('=' in a):
        a = b64d(a)
        io.sendline(a)
    elif(re.search('[0-1]{8}',a)):
        ascii_string = "".join([chr(int(binary, 2)) for binary in a.split(" ")])
        io.sendline(ascii_string)
    elif(re.search('0[0-9]{3}',a)):
        ascii_string = "".join([chr(int(binary, 8)) for binary in a.split(" ")])
        io.sendline(ascii_string)
    elif('0x' in a):
        ascii_string = b"".join([unhex(binary[2:]) for binary in a.split(" ")])
        io.sendline(ascii_string)
    elif(re.search('[0-9]{2,3}',a)):
        ascii_string = "".join([chr(int(binary)) for binary in a.split(" ")])
        io.sendline(ascii_string)
    else:
        log.info("NOT DETECTED")
        skip=1

while(True):
    if(skip!=0):
        break
    io.recvuntil(b"encoding: ")
    a = io.recv().decode('utf-8')
    log.info("A is: "+a)
    decodeNsend(a)

log.info("I AM BROKE")