# def DFS(x):
#     global cnt
#     ch[x]=cnt
    
#     for i in range(1,n+1):
#         if graph[x][i]==1 and ch[i]==0:
#             cnt+=1
#             DFS(i)
    

# n,m,r=map(int,input().split())

# graph=[[2]*(n+1) for _ in range(n+1)]

# for _ in range(m):
#     a,b=map(int,input().split())
#     graph[a][b]=1
# cnt=1
# ch=[0]*(n+1)
# DFS(r)

# for i in range(1,n+1):
#     print(ch[i])
#########################

def dfs(t):
    global cnt
    ch[t] = cnt
    graph[t].sort()
    for i in graph[t]:
        if ch[i] == 0:
            cnt += 1
            dfs(i)

import sys
sys.setrecursionlimit(150000)
N, M, R = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
ch = [0]*(N+1)  # 저장값
cnt = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # 양 방향 간선
    graph[b].append(a)  # 양 방향 간선
dfs(R)
for i in range(1, N+1):
    print(ch[i])



