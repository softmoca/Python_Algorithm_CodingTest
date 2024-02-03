def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a>b:
        parent[a]=b
    else:
        parent[b]=a

def find_parent(parent,x):
    if parent[x] != x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]


n,m=map(int,input().split())
edges=[]

parent=[0]*(n+1)

for i in range(n+1):
    parent[i]=i


for _ in range(m):
    a,b,c=map(int,input().split())
    edges.append((c,[a,b]))

edges.sort()



res=[]
for i in range(m):
    if find_parent(parent,edges[i][1][0])==find_parent(parent,edges[i][1][1]):
        continue
    else:
        res.append(edges[i])
        union(parent,edges[i][1][0],edges[i][1][1])
        
res.pop()

S=0
for i in range(len(res)):
    S+=res[i][0]
print(S)















