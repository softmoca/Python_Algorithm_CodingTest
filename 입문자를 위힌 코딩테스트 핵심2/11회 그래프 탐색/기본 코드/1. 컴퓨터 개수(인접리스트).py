cnt=1
def DFS(x,ch,grapgh):
    global cnt
    
    ch[x]=1
    for i in grapgh[x]:
        if ch[i]==0:
            ch[i]=1
            cnt+=1
            DFS(i,ch,grapgh)


def solution(n, edges):
    global cnt
    answer = 0

    graph=[[] for _ in range(n+1)]

    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    cnt=1
    ch=[0]*(n+1)
    DFS(1,ch,graph)



    
    return n-cnt
                    

print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))

