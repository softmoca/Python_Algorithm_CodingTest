def DFS(n):
    if n==1 or n==2:
        return 1
    else:
        return DFS(n-1)+DFS(n-2)
    
              
print(DFS(8))

