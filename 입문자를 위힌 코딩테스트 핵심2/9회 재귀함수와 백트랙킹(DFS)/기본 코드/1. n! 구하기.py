def DFS(n):
    if n==1:
        return 1
    else:
        return DFS(n-1)*n
    

print(DFS(5))             
print(DFS(6))
