n,m=map(int,input().split())
x,y,d=map(int,input().split())

arr=[list(map(int, input().split())) for _ in range(m)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
d=0
cnt=1

while True:
    flag=0
    for d in range(4):
        d=(d+3)%4
        nx=x+dx[d]
        ny=y+dy[d]
        if arr[nx][ny]==0:
            flag=1
            x=nx
            y=ny
            arr[nx][ny]=1
            cnt+=1
    if flag==0:
        break

print(cnt)




