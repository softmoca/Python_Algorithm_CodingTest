def dfs(t):
    global cnt
    ch[t] = cnt
    graph[t].sort(reverse=True)
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
