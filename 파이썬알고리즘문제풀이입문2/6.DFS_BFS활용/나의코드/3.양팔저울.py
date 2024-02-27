def DFS(L,summ):
    if L==n:
        res[abs(summ)]=1
    else:
        for i in range(n):
            DFS(L+1,summ+arr[L])
            DFS(L+1,summ)
            DFS(L+1,summ-arr[L])
     




n=int(input())
arr=list(map(int,input().split()))
res=[0]*(sum(arr)+1)
ch=[0]*n

DFS(0,0)


cnt=0
for i in range(len(res)):
    if res[i]==0:
        cnt+=1

print(cnt)
