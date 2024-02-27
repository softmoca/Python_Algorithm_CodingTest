from collections import deque

arr1=list(map(str,input()))
n=int(input())
dq=deque(arr1)


for i in range(1,n+1):
    dq=deque(arr1)
    s=input()
    for x in s:
        if dq and x==dq[0]:
            dq.popleft()
    
    if dq:
        print(f'#{i} NO')
    else:
        print(f'#{i} YES')






