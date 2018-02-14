import time
import math
timetaken = time.time()
f = open('sawyr10.txt')
d = {}
a = input('please input the number of character you want to calculate: ')
if a == 1:
    for i in range(97,123):
        d[chr(i)] = 0

    lines = f.readlines()
    for line in lines:
        for i in line:
            t = i.lower()
            if ord(t) in range(97,123):
                d[t]+=1
elif a == 2:
    for i in range(97,123):
        for j in range(97,123):
            d[chr(i)+chr(j)] = 0

    lines = f.readlines()
    for line in lines:
        for i in range(0,len(line)-1):
            t1 = line[i].lower()
            t2 = line[i+1].lower()
            if ord(t1) in range(97,123) and ord(t2) in range(97,123):
                d[t1+t2]+=1
elif a == 3:
    for i in range(97,123):
        for j in range(97,123):
            for m in range(97,123):
                d[chr(i)+chr(j)+chr(m)] = 0
    lines = f.readlines()
    for line in lines:
        for i in range(0,len(line)-2):
            t1 = line[i].lower()
            t2 = line[i+1].lower()
            t3 = line[i+2].lower()
            if ord(t1) in range(97,123) and ord(t2) in range(97,123) and ord(t3) in range(97,123):
                d[t1+t2+t3]+=1

else:
    print(a, 'is not a correct input')

f.close()
ans = 0
for i in d:
    ans+=d[i]
d_fre = {}
for i in d:
    d_fre[i] = d[i]/ans

d_h={}
for i in d_fre:
    if d_fre[i] > 0.0001:
        d_h[i] = -d_fre[i]*math.log(d_fre[i], 2)
    else:
        d_h[i] = 0

time = time.time()- timetaken
print('time consumed:', time)
