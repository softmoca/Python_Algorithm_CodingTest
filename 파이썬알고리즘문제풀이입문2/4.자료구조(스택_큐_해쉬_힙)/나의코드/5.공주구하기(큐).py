from collections import deque

n,m=map(int,input().split())
dq=deque(range(1,n+1))
while True:
    for _ in range(m-1):
        cur=dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq)==1:
        break
print(dq[0])






