def DFS(x,y,arr):
    arr[x][y]=1
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0:
            DFS(nx,ny,arr)


n,m=map(int,input().split())

arr=[list(map(int,input())) for _ in range(n)]
cnt=0

for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            
            cnt+=1
            DFS(i,j,arr)



print(cnt)





