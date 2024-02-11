def DFS(L,s):
    global cnt
    if L==k:
        if sum(res)%m==0:
            cnt+=1
       
    else:
        for i in range(s,n):
            res[L]=arr[i]
            DFS(L+1,i+1)
        
n,k=map(int,input().split())
arr=list(map(int,input().split()))
m=int(input())

res=[0]*k
cnt=0
DFS(0,0)

print(cnt)