from collections import deque


n=int(input())
arr=[list(map(int,input())) for _ in range(n)]

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
block_cnt=0
res=[]


for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            block_cnt+=1
            dq=deque()
            dq.append([i,j])
            arr[i][j]=0
            cnt=1
            while dq:
                
                for _ in range(len(dq)):
                    x,y=dq.popleft()
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]

                        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
                            arr[nx][ny]=0
                            dq.append([nx,ny])
                            cnt+=1
            res.append(cnt)
print(block_cnt)
for x in res:
    print(x)












