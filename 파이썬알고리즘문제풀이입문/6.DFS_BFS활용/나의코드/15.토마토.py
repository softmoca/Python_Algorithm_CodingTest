from collections import deque

n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(m)]

dq=deque()
for i in range(m):
    for j in range(n):
        if arr[i][j]==1:
            dq.append([i,j])
L=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

while dq:
    L+=1
    print(dq)
    for _ in range(len(dq)):
        x,y=dq.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<m and 0<=ny<n and arr[nx][ny]==0:
                arr[nx][ny]=1
                dq.append([nx,ny])

for i in range(m):
    for j in range(n):
        if arr[i][j]==0:
            print(-1)
            

print(L-1)



