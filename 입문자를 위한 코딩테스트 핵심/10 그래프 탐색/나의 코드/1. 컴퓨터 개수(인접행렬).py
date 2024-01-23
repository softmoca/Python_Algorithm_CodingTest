def DFS(x,y,arr,cnt):
    
    cnt.append(x)
    cnt.append(y)
    #print(x,y)
    arr[x][y]=0
    arr[y][x]=0
    
    for i in range(1,len(arr)):
        if arr[y][i]==1:
            DFS(y,i,arr,cnt)



def solution(n, edges):
    answer = 0
    cnt=[]
    arr=[[0]*(n+1) for _ in range(n+1)]    
    for x in edges:
        arr[x[0]][x[1]]=1
        arr[x[1]][x[0]]=1
    
    for i in range(1,n+1):
        if arr[1][i]==1:
            DFS(1,i,arr,cnt)
    answer=n-len(set(cnt))
    
    return answer
                    

print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))
