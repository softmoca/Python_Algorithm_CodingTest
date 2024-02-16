from collections import deque

n=int(input())

dq=deque(list(range(1,n+1)))


while True:
    if n==1:
        print(1)
        break
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        break
    dq.append(dq.popleft())








