from collections import deque
n=int(input())

arr=[list(map(int,input().split())) for _ in range(n) ]

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
dq=deque()
res=[]
cnt=0

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            cnt+=1
            arr[i][j]=0
            dq.append([i,j])

            while dq:
                for w in range(len(dq)):
                    x,y=dq.popleft()

                    for k in range(8):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
                            arr[nx][ny]=0
                            dq.append([nx,ny])
            

print(cnt)
    






