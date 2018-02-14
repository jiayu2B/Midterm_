import math
import time
tim = time.time()
_list = []
t = ''
def win(t):
    
    if t.count('A') == 3 or t.count('B') == 3:
        _list.append(t)
        return
    win(t+'A')
    win(t+'B')
    
win(t)
    
print('the X are: ', _list)
arr = [[],[],[]]
for i in _list:
    if len(i) == 3:
        arr[0].append(i)
    elif len(i) == 4:
        arr[1].append(i)
    if len(i) == 5:
        arr[2].append(i)
print('Fre(Y=3) = ',len(arr[0]))
print('Fre(Y=4) = ',len(arr[1]))
print('Fre(Y=5) = ',len(arr[2]))

print('H(X) = ', math.log(len(_list), 2))

ans = 0
for i in range(3):
    ans += len(arr[i])/len(_list) * math.log(len(arr[i])/len(_list), 2)*(-1)
print('H(Y) = ', ans)
print('H(Y|X) = ', 0) #For when we know X, we know Y already
print('H(X|Y) = ', math.log(len(_list), 2)-ans)#by Venn graph, Y is inside the graph of X.
print('I(X;Y) = ', ans)#by chain rules

print('time consumed',time.time()-tim)
