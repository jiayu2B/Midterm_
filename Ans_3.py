import time
from compress import LZW
from decompress import decom
import os
def compress(filename='test.txt'):
    timetaken = time.time()
    f = open(filename, "r")
    lines = f.read()
    print(len(lines))
    leng = len(lines)
    t = int(leng/50000)
    for i in range(0,t+1):
        LZW(i, filename)
    timetaken = time.time() - timetaken
    print(timetaken)
    size = 0
    for i in range(t+1):
        size += os.path.getsize("compressed_read"+str()+".bin")
    print ('the ratio is: ', size/ os.path.getsize(filename))
    
def decompress(t=8, filename = 'compressed_read.bin'):
    timetaken = time.time()
    f = open('decom.txt','wb')
    a = ''
    for i in range(0,t+1):
        a+=decom(i, filename)
    print(len(a))
    f.write(bytes(a, 'utf-8'))
    f.close()
    timetaken = time.time() - timetaken
    print(timetaken)
