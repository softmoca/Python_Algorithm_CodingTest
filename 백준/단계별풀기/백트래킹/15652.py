










def DFS(L,s):
    if L==m:
        for x in res:
            print(x,end=' ')
        print()
    else:
        for i in range(s,n+1):
                res[L]=i
                DFS(L+1,i)
             
          

n,m=map(int,input().split())
res=[0]*m

DFS(0,1)
