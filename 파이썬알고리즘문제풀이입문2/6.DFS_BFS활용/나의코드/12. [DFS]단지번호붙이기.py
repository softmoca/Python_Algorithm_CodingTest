def DFS(x,y):
   
    global cnt
    cnt+=1

    arr[x][y]=0
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
            DFS(nx,ny)



n=int(input())
arr=[list(map(int,input())) for _ in range(n)]
res=[]
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
block_cnt=0

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            block_cnt+=1
            cnt=0
            DFS(i,j)
            res.append(cnt)

print(block_cnt)
for x in res:
    print(x)