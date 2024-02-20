def DFS(L,s):
    global Minn
    if L==m:
        S=0
        for i in range(len(h)):
            Minnn=10000
            x,y=h[i]
            for j in res:
                temp2=abs(x-p[j][0]) +abs(y-p[j][1]) 
                if Minnn>temp2:
                    Minnn=temp2
            S=S+Minnn
        if S<Minn:
            Minn=S
    else:
        for i in range(s,PCount):
            res[L]=i
            DFS(L+1,i+1)

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

PCount=len(p)
res=[0]*(m)
DFS(0,0)
print(Minn)












