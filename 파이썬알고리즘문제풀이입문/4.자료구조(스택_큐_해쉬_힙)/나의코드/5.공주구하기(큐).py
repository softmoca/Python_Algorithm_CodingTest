from collections import deque


n,m=map(int,input().split())

dq=deque()

for i in range(1,n+1):
    dq.append(i)


while True:
    for i in range(m-1):
        dq.append(dq.popleft())
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        break

