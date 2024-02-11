from collections import deque


arr=[list(map(int,input().split())) for _ in range(7) ]
# ch=[[0]*7 for _ in range(7)]

dq=deque()

dq.append((0,0))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
arr[0][0]=1
while dq:

    for i in range(len(dq)):
        x,y=dq.popleft()
        if x==6 and y==6:
            print(arr[6][6]-1)
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<7 and 0<= ny <7 and arr[nx][ny]==0:
                dq.append((nx,ny))
                arr[nx][ny]=arr[x][y]+1






