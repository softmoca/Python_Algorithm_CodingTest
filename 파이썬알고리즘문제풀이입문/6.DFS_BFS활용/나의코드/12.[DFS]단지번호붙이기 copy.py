def DFS(x,y):
    global cnt
    cnt+=1
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
            arr[nx][ny]=0
            
            DFS(nx,ny)


n=int(input())
arr=[list(map(int,input())) for _ in range(n)]
res=[]
cnt2=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(n):
    for j in range(n):
        cnt=0
        
        if arr[i][j]==1:
            arr[i][j]=0
            DFS(i,j)
            cnt2+=1
            res.append(cnt)
            
print(cnt2)
for x in res:
    print(x)

