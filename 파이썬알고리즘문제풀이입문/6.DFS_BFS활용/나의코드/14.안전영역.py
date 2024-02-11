def DFS(x,y):
    ch[x][y]=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0:
            ch[nx][ny]=1
            DFS(nx,ny)

res=[]
n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for h in range(1,101):
    ch=[[0]*n for _ in range(n)]
    cnt=0
    for i in range(n):
        for j in range(n):
            if arr[i][j]<=h:
                ch[i][j]=1
    for i in range(n):
        for j in range(n):
            if ch[i][j]==0:
                ch[i][j]=1
                cnt+=1
                DFS(i,j)
    
    res.append(cnt)
print(max(res))
    





