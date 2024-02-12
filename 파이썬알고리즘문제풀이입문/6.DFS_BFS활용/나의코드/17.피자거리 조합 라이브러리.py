from itertools import combinations
n,m=map(int,input().split())

arr=[list(map(int,input().split())) for _ in range(n)]
h=[]
p=[]
Minn=10000
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            h.append([i,j])
        if arr[i][j]==2:
            p.append([i,j])

res=list(combinations(p,m))



for x in res:
    S=0
    for i in range(len(h)):
        Minnn=10000
        hx,hy=h[i]
        for k in range(m):
            temp2=abs(hx-x[k][0]) +abs(hy-x[k][1])
            if Minnn>temp2:
                Minnn=temp2
        S=S+Minnn
    if S<Minn:
        Minn=S

print(Minn)


