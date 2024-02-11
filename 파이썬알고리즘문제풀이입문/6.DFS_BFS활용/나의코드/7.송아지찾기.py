from collections import deque
import sys

s,e=map(int,input().split())
dq=deque()
dq.append(s)
L=0

while dq:
    
    for i in range(len(dq)):
        x=dq.popleft()
        if x==e:
            print(L)
            sys.exit()
        
        dq.append(x-1)
        dq.append(x+1)
        dq.append(x+5)
    L+=1

print(L)



