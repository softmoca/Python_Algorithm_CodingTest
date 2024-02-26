n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
for x in arr:
    x.append(0)
    x.insert(0,0)

arr.insert(0,[0]*(n+2))
arr.append([0]*(n+2))

dx=[-1,0,1,0]
dy=[0,1,0,-1]
cnt=0

for i in range(1,n+1):
    for j in range(1,n+1):
        flag=0
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if arr[i][j]>arr[nx][ny]:
                continue
            else:
                flag=1
        if flag==0:
            cnt+=1
print(cnt)



