def DFS(v,graph,ch,n):
    global cnt

    if v==n:
        cnt+=1
    else:
        for x in graph[v]:
            if ch[x]==0:
                ch[x]=1
                DFS(x,graph,ch,n)
                ch[x]=0




n,m=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)

ch=[0]*(n+1)
cnt=0
ch[1]=1
DFS(1,graph,ch,n)
print(cnt)


