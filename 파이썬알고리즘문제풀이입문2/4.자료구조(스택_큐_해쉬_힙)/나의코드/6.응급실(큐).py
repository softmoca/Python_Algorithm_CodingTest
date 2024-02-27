from collections import deque

n,m=map(int,input().split())

dq=deque()

arr=list(map(int,input().split()))

for i in range(n):
    dq.append([i,arr[i]])



cnt=0
while True:
    M=max(x[1] for x in dq)

    

    if dq[0][1]==M:
        if dq[0][0]==m:
            print(cnt+1)
            break
        dq.popleft()
        cnt+=1

    else:
        dq.append(dq.popleft())








