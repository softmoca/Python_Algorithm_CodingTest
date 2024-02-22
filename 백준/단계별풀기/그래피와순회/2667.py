def DFS(x,y):
    
    global cnt
    cnt+=1

    ch[x][y]=1
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]

        if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0 and arr[nx][ny]==1:
            DFS(nx,ny)
    

n=int(input())
arr=[list(map(int,input())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
cnt=0
res=[]
cnt2=0
for i in range(n):
    for j in range(n):
        if arr[i][j]==1 and ch[i][j]==0:
            cnt2+=1
            cnt=0
            ch[i][j]=1
            DFS(i,j)
            res.append(cnt)

print(cnt2)
res.sort()
for x in res:
    print(x)






