def DFS(L,summ):
    global Minn
    if L > Minn:
        return

    if summ==m:
        if Minn>L:
            Minn=L
    else:
        for i in range(n):
            DFS(L+1,summ+arr[i])



n=int(input())

arr=list(map(int,input().split()))
arr.sort(reverse=True)
m=int(input())

Minn=10000
DFS(0,0)
print(Minn)


