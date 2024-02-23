import heapq
import sys


def da(start):
    dis=[INF]*(V+1)
    dis[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,now=heapq.heappop(q)
        
        if dis[now]<dist:
            continue

        for i in graph[now]:
            cost = dist+i[1]

            if cost<dis[i[0]]:
                dis[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    return dis

V,E=map(int,input().split())
start=int(input())


graph=[[] for _ in range(V+1)]

for _ in range(E):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

INF=1e9


arr=da(start)

print(arr)




