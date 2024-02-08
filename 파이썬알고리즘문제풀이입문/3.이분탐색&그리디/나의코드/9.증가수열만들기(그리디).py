from collections import deque

n=int(input())
arr=list(map(int,input().split()))

res=[]
dq=deque(arr)
res=[[0,'T']]

for _ in range(n):
    print(dq,res)
    if dq[0]<dq[-1] :# 왼쪽이 작은경우 
        if dq[0]>res[-1][0]: # 
            res.append([dq[0],'L'])
            dq.popleft()
        elif dq[-1]>res[-1][0]:
            res.append([dq[-1],'R'])
            dq.pop()

    elif dq[0] > dq[-1]:
        if dq[-1]>res[-1][0]:
            res.append([dq[-1],'R'])
            dq.pop()
        elif dq[0]>res[-1][0]:
            res.append([dq[0],'L'])
            dq.popleft()

print(len(res)-1)

for i in range(1,len(res)):
    print(res[i][1],end='')



