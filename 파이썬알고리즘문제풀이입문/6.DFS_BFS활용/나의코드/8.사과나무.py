from collections import deque

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
ch=[[0]*n for _ in range(n)]

dq=deque()
dq.append((n//2,n//2))
S=arr[n//2][n//2]
L=0
ch[n//2][n//2]=1
while dq:
    if L==n//2:
        break
    for _ in range(len(dq)):
        x,y=dq.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if  0<=nx<n and 0<=ny <n and ch[nx][ny]==0:
                ch[nx][ny]=1
                dq.append((nx,ny))
                S=S+arr[nx][ny]
    L+=1
    
print(S)



