from collections import deque


n,k=map(int,input().split())

res=[]
dq=deque(list(range(1,n+1)))

while len(dq)!=1:
    for _ in range(k-1):
        
        dq.append(dq.popleft())
    res.append(dq.popleft())

res.append(dq.popleft())


print("<",end='')

for x in res:
    if x==res[-1]:
        print(x,end='')
        print(">")

    else:
        print(x,end='')
        print(",",end=' ')



