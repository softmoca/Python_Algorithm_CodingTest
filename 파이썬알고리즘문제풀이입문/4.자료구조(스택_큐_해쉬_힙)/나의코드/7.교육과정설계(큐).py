from collections import deque
arr=list(input())
n=int(input())

for i in range(1,n+1):
    dq=deque(arr)
    temp=list(input())
    for x in temp:
        if dq and x==dq[0]:
            dq.popleft()
    if dq:
        print("# %d No" %(i))
    else:
        print("# %d Yes" %(i))
    

        
   







