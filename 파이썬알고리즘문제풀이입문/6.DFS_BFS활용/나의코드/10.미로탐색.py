def DFS(x,y):
    global cnt
    if x==6 and y==6:
        cnt+=1
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<7 and 0<=ny<7 and ch[nx][ny]==0 and arr[nx][ny]==0:
            ch[nx][ny]=1
            DFS(nx,ny)
            ch[nx][ny]=0



arr=[list(map(int,input().split())) for _  in range(7)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

ch=[[0]*7 for _ in range(7)]

cnt=0
ch[0][0]=1
DFS(0,0)
print(cnt)







