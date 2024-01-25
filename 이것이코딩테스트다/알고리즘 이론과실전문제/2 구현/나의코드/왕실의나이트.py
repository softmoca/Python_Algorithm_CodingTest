col,row=(map(str,input()))

col=ord(col)
col=col-96
row=int(row)

arr=[[0]*9 for _ in range(9)]
cnt=0

dx=[-2,-2,-1,1,2,2,1,-1]
dy=[-1,1,2,2,1,-1,-2,-2]

for k in range(8):
    nx=row +dx[k]
    ny=col+dy[k]
    if 1<=nx<9 and 1<=ny<9:
        cnt+=1

print(cnt)