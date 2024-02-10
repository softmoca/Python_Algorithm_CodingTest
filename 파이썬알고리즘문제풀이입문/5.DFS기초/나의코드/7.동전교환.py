def DFS(L,summ):
    if summ==m:
        print(L)
        return
    else:
        for i in range(n):
            DFS(L+1,summ+arr[i])


n=int(input())
arr=list(map(int,input().split()))
m=int(input())

Minn=500

arr.sort(reverse=True)
DFS(0,0)



