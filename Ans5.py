import math
import time
tim = time.time()
H = {}
for i in range (1,27):
    p =0.2594424254818772/i
    H[chr(i+96)]= -p*math.log(p, 2)
print(H)
print('Time consumed',time.time()-tim)

