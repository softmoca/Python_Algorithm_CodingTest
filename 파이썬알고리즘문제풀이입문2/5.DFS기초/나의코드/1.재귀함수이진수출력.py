def DFS(x):
    
    if x==0:
        return
    else:
        res.append(x%2)
        DFS(x//2)

res=[]
n=int(input())
DFS(n)


for _ in range(len(res)):
    print(res.pop(),end='')