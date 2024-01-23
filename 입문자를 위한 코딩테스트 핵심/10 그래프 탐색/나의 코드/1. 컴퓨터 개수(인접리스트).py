cnt=0

def DFS(v,ch,arr,n):
    ch[v]=1
    global cnt
    cnt+=1
    for i in range(1,n+1):
        for x in arr[v]:
            if ch[i]==0 and x==i:
                DFS(i,ch,arr,n)

def solution(n, edges):
    answer = 0

    arr=[[]*(n+1) for _ in range(n+1)]
    
    for [a,b] in edges:
        arr[a].append(b)
        arr[b].append(a)
    
    ch=[0]*(n+1)
    global cnt
    cnt=0
    DFS(1,ch,arr,n)    
    
    return n-cnt
        
                    
print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))

