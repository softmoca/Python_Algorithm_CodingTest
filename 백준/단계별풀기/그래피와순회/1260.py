from collections import deque

def DFS(x):
    global cnt
    ch1[x]=cnt

    for w in graph[x]:
        if ch1[w]==0:
            cnt+=1
            ch1[w]=cnt
            DFS(w)




n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()
cnt=1
ch1=[0]*(n+1)


DFS(v)



for i in range(1,n+1):
    print(ch1[i],end=' ')
print()


ch2=[0]*(n+1)
dq=deque()
cnt=1
dq.append(v)
ch2[1]=1
while dq:
    x=dq.popleft()

    for w in graph[x]:
        if ch2[w]==0:
            cnt+=1
            ch2[w]=cnt
            dq.append(w)

for i in range(1,n+1):
    print(ch2[i],end=' ')


