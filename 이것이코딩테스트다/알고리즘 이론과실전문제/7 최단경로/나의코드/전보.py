import heapq

n,m,c=map(int,input().split())
graph=[[] for _ in range(n+1)]
dis=[30000]*(n+1)

for i in range(m):
    a,b,d=map(int,input().split())
    graph[a].append((b,d))

def dijkstra(start):
   
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        if dis[now]<dist:
            continue
        for i in graph[now]:
            cost =dist+i[1]
            if cost < dis[i[0]]:
                
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))


dijkstra(c)
cnt=0
M=0

for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if dis[i] == 30000:
       continue
    # 도달할 수 있는 경우 거리를 출력
    else:
        cnt+=1
        if M<dis[i]:
            M=dis[i]

print(cnt, M)



