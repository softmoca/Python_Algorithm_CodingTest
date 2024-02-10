def DFS(L):
    if L==n:
        S=0
        for i in range(n):
            
            S=S+(res[i]*arr1[i])
        if S==m:
            print(res)
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0

n,m=map(int,input().split())

res=[0]*n
ch=[0]*(n+1)


arr1=[0]*n
arr1[0]=1
arr1[n-1]=1

for i in range(1,n):
    arr1[i]=arr1[i-1]*(n-i)//i

DFS(0)