from collections import deque
import sys

n=int(input())
dq=deque()

for _ in range(n):
    arr=list(map(int,sys.stdin.readline().split()))

    if len(arr)==2:
        if arr[0]==1:
            dq.appendleft(arr[1])
        else:
            dq.append(arr[1])
    else:
        if arr[0]==3:
            if dq:
                print(dq.popleft())
            else:
                print(-1)
        elif arr[0]==4:
            if dq:
                print(dq.pop())
            else:
                print(-1)
        elif arr[0]==5:
            print(len(dq))
        elif arr[0]==6:
            if dq:
                print(0)
            else:
                print(1)
        elif arr[0]==7:
            if dq:
                print(dq[0])
            else:
                print(-1)
        elif arr[0]==8:
            if dq:
                print(dq[-1])
            else:
                print(-1)




