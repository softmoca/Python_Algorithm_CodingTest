def DFS(x,summ):
    global M
    if summ>c:
         return
    if x==n: 
        if summ>M:
                M=summ
    else:
        DFS(x+1,summ+arr[x])
        DFS(x+1,summ)

c,n=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))
M=0
DFS(0,0)
print(M)
