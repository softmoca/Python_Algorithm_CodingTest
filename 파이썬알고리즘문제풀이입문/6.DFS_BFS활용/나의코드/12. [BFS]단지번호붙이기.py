from collections import deque

n=int(input())
arr=[list(map(int,input())) for _ in range(n)]
res=[]

cnt2=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

dq=deque()

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            cnt2+=1
            dq.append([i,j])
            cnt=0

            while dq:
                for i in range(len(dq)):
                    x,y=dq.popleft()
                    
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
                            arr[nx][ny]=0
                            dq.append((nx,ny))
                            cnt+=1
            res.append(cnt)


print(res,cnt2)









