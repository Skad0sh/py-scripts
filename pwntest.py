from pwn import *
import re
import hashlib

context.log_level='debug'
io = remote('159.65.156.133',1337)
i = 0
#LEVEL 1
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

while(i < 10):
    a = io.recvuntil(b"encoding: ")
    a = io.recv().decode('utf-8')
    decodeNsend(a)
    i += 1

i = 0
# LEVEL 2
while(i < 10):
    a = io.recvuntil(b'caeser ')
    a = io.recv().decode('utf-8')
    cipher = a[:5]
    key = int(a[15:])
    decoded = ""
    for char in cipher:
        if((ord(char)-key)<97):
            decoded += chr(122-((key-1)-(ord(char)-97)))
        else:
            decoded += chr(ord(char)-key)
    log.info(decoded)
    io.sendline(decoded)
    i += 1

i = 0
#LEVEL 3
with open('threeword.txt','r+',encoding='utf-8') as f:
    while(i < 10):
        a = io.recvuntil(b'hash: ')
        a = io.recv().decode('utf-8')[:-1]
        if(len(a)==32):
            for line in f:
                bruthash = hashlib.md5(line[:-1].encode('utf-8')).hexdigest()
                if(a==bruthash):
                    print("match: "+line)
                    io.sendline(line)
        elif(len(a)==64):
            for line in f:
                bruthash = hashlib.sha256(line[:-1].encode('utf-8')).hexdigest()
                if(a==bruthash):
                    print("match: "+line)
                    io.sendline(line)
        elif(len(a)==128):
            for line in f:
                bruthash = hashlib.sha512(line[:-1].encode('utf-8')).hexdigest()
                if(a==bruthash):
                    print("match: "+line)
                    io.sendline(line)
        elif(len(a)==40):
            for line in f:
                bruthash = hashlib.sha1(line[:-1].encode('utf-8')).hexdigest()
                if(a==bruthash):
                    print("match: "+line)
                    io.sendline(line)
        i += 1