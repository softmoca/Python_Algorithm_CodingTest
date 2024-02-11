def DFS(x,y):
    global cnt
    if x==Maxij[0] and y==Maxij[1]:
        cnt+=1
    else:
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<n and ch[nx][ny]==0 and arr[nx][ny]>arr[x][y]:
                ch[nx][ny]=1
                DFS(nx,ny)
                ch[nx][ny]=0


n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

Maxx=0
Minn=100
Maxij=[]
Minij=[]

for i in range(n):
    for j in range(n):
        if arr[i][j]>Maxx:
            Maxx=arr[i][j]
            Maxij=[i,j]
        if arr[i][j]<Minn:
            Minn=arr[i][j]
            Minij=[i,j]
cnt=0
DFS(Minij[0],Minij[1])

print(cnt)




