def DFS(L):
    if L==m:
        for x in res:
            print(x,end=' ')
        print()
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0
          
            






n,m=map(int,input().split())
ch=[0]*(n+1)
res=[0]*m

DFS(0)







