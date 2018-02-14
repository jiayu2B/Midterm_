from struct import *
def LZW(t, filename):
    f = open(filename, "r")
    lines = f.read()
    content = lines[t*50000:(t+1)*50000]
    length = len(content)
    f.close()
    
    codes=[]
    for i in range(0,256):
        codes.append(chr(i))
    filename = "compressed_read"+str(t)+".bin"
    f1 = open(filename, "wb")
    cs = ""
    ans = ""

    for i in range(0,length) :
        tem = cs + content[i]
        if tem in codes :
            cs += content[i]
        else :
            codes.append(cs + content[i])
            binary = pack('h', codes.index(cs))
            ans += codes[codes.index(cs)]
            f1.write(binary)
            cs = content[i]
    f1.write(pack('h', codes.index(cs)))
    f1.close()

