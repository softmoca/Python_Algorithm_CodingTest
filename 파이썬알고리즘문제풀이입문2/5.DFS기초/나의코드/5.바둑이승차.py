def DFS(L,summ):
    if summ>c:
        return

    if L==n:
        res.append(summ)


    else:
        DFS(L+1,summ+arr[L])
        DFS(L+1,summ)

c,n=map(int,input().split())

arr=[]
for _ in range(n):
    arr.append(int(input()))

res=[]
DFS(0,0)
print(max(res))




