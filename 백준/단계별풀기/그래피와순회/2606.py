from collections import deque



n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dq=deque()

dq.append(1)
ch=[0]*(n+1)
ch[1]=1

while dq:
    x=dq.popleft()
    
    for w in graph[x]:
        if ch[w]==0:
            dq.append(w)
            ch[w]=1


ch[1]=0
print(sum(ch))




