from collections import deque



arr=[list(map(int,input().split())) for _ in range(7)]
dis=[[0]*7 for _ in range(7)]

dq=deque()

dq.append([0,0])
dx=[-1,0,1,0]
dy=[0,1,0,-1]
arr[0][0]=1

while dq:
    for _ in range(len(dq)):
        x,y=dq.popleft()

        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            if 0<=nx<7 and 0<=ny<7 and arr[nx][ny]==0:
                dq.append([nx,ny])
                arr[nx][ny]=1
                dis[nx][ny]=dis[x][y]+1


print(dis[6][6])




