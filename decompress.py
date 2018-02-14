def decom(t, filename):
    f = open(filename[:-4]+str(t)+filename[-4::], "rb")
    lines = f.read()
    f.close()
    codes = []
    for i in range(0, 256) :
        codes.append(chr(i))
    val = lines[0] + lines[1] + (lines[1])*255
    res = codes[val]
    tem = codes[val]
    for i in range(3, len(lines), 2):
        val = lines[i-1] + lines[i] + (lines[i])*255
        if(val < len(codes)):
            res +=codes[val]
            codes.append(tem + codes[val][0])
            tem = codes[val]
        else:
            codes.append(tem + tem[0])
            res += (tem + tem[0])
        tem = codes[val]
    return res
