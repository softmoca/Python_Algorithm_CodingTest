def union(parent,a,b):
    a=check_parent(parent,a)
    b=check_parent(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a 
    
def check_parent(parent,x):
    if parent[x] !=x:
        parent[x]=check_parent(parent,parent[x])
    return parent[x] 

n,m=map(int,input().split())

parent=[0]*(n+1)

for i in range(n+1):
    parent[i]=i

for i in range(m):
    a,b,c=map(int,input().split())
    if a== 0:
        union(parent,b,c)
    if a==1:
        if  check_parent(parent,b) ==check_parent(parent,c):
            print("YES")
        else:
            print("NO")

