import time
import bitarray
import os
a = input("1 for compress. 0 for decompress: ")
x = 1

if a == '1':
    _file = input('input the name of file you want to compress:')
    x = input("1 for 1 character. 2 for 2 character. 3 for 3 character: ")

if x== '1':
    from Huffman import *
elif x == '2':
    from Huffman2 import *
else:
    from Huffman3 import *

if a == '1':
    tie = time.time()
    f = open(_file, 'r')
    line=f.read()
    tree= Tree(line)
    d={}
    build_Dict(tree,'',d)
    dic = open('dict.txt','w')
    json.dump(d,dic)
    text = compress(line, d)
    b = bitarray.bitarray(text)
    com = open('compressed.Huffman','wb')
    c=b.tobytes()
    com.write(c)

    f.close()
    dic.close()
    com.close()

    print('compress finish')
    fsize =(os.path.getsize('compressed.Huffman')+os.path.getsize('dict.txt'))/os.path.getsize(_file)
    print('compress ratio:', fsize)
    print('time used:', time.time()-tie)
if a == '0':
    tie = time.time()
    f = open('compressed.Huffman','rb')
    b=bitarray.bitarray()
    bs=f.read()
    b.frombytes(bs)
    content=b.to01()
    f.close()
    f1 = open('dict.txt','r') 
    _dict=json.load(f1)
    dc = decompress(content,_dict)
    f1.close()
    f2 = open('test_decompress.txt','w')
    f2.write(dc)
    f2.close()
    print ("decompression finish")
    print('time used:', time.time()-tie)
