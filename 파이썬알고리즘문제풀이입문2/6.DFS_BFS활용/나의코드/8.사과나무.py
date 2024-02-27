from collections import deque


n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]

dq=deque()
start,end=n//2,n//2
ch[start][end]=1
dq.append([start,end])
S=arr[start][end]
L=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

while dq:
    if L==n//2:
        break
    for _ in range(len(dq)):
        x,y=dq.popleft()


        for k in range(4):
            nx=x+dx[k]
            ny=y + dy[k]

            if 0<=nx<n and 0<=ny <n and ch[nx][ny]==0:
                ch[nx][ny]=1
                S=S+arr[nx][ny]
                dq.append([nx,ny])
    L+=1
print(S)











