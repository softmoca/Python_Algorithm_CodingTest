def DFS(L,s):
    if L==n:
        print(ch)
    else:
        for i in range(1,n+1):
            if graph[s][i]:
                ch[i]=1
                DFS(L+1,i)
                ch[i]

n,m=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

ch=[0]*(n+1)
cnt=0
DFS(0,1)




