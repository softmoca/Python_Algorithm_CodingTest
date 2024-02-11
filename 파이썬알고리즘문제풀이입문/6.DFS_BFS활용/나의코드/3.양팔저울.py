def DFS(L,res):
    if L==k:
        if res>0:
            ch[res]=1
    else:
        DFS(L+1,res-arr[L])
        DFS(L+1,res)
        DFS(L+1,res+arr[L])
    

k=int(input())
arr=list(map(int,input().split()))
S=sum(arr)
ch=[0]*(S+1)

DFS(0,0)
print(S-sum(ch))

