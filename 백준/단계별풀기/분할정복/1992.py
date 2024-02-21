def DFS(x,y,n):
    color=arr[x][y]
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if arr[i][j]!=color:
                res.append('(')
                DFS(x,y,n//2)
                DFS(x,y+n//2,n//2)
                DFS(x+n//2,y,n//2)
                DFS(x+n//2,y+n//2,n//2)
                res.append(')')
                return
    if color==1:
        res.append(1)
    else:
        res.append(0)
    
res=[]
n=int(input())
arr=[list(map(int,input()))   for _ in range(n) ]
DFS(0,0,n)

for x in res:
    print(x,end='')








