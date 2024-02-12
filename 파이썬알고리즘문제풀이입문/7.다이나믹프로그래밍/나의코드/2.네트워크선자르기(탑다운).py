def DFS(L):
    if L==1 or L==2:
        return L
    else:
        return DFS(L-1)+DFS(L-2)
   

n=int(input())


print(DFS(n))