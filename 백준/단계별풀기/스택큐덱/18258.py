from collections import deque
import sys

n=int(input())
dq=deque()
for _ in range(n):
    arr=list(map(str,sys.stdin.readline().split()))
    
    if len(arr)==2:
        dq.append(arr[1])
    else:
        if arr[0]=='pop':
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif arr[0]=='size':
            print(len(dq))
        elif arr[0]=='empty':
            if dq:
                print(0)
            else:
                print(1)
        elif arr[0]=='front':
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif arr[0]=='back':
            if dq:
                print(dq[-1])
            else:
                print(-1)
                






