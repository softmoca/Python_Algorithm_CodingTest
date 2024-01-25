N=int(input())

arr=[[0]*N for _ in range(N)]

plan=list(map(str,input().split()))
x,y=0,0
dx=[-1,0,1,0]
dy=[0,1,0,-1]

dir=['U','R','D','L']

for z in plan:
    for k in range(4):
        if z==dir[k]:
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<N and 0<=ny<N:
                x=nx
                y=ny

print(x+1,y+1)
            




