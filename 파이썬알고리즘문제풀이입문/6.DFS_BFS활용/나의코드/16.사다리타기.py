def DFS(x,y):
    if x==0:
        print(y)

    if 0<=y+1<10 and arr[x][y+1]==1:
        arr[x][y+1]=0
        DFS(x,y+1)
    elif 0<=y-1<10 and arr[x][y-1]==1:
        arr[x][y-1]=0
        DFS(x,y-1)
    elif 0<=x-1<10 and arr[x-1][y]==1:
        
        arr[x-1][y]=0
        DFS(x-1,y)


arr=[list(map(int,input().split())) for _ in range(10)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]

for i in range(10):
    if arr[9][i]==2:
        arr[9][i]=0
        DFS(9,i)










