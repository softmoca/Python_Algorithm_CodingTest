def DFS(L,s):
    global Minn
    if L==m:

        temp=0
        for i in range(len(h)):
            temp2=0
            Minnn=10000
            x,y=h[i]
            for j in res:
                temp2=temp2+(abs(x-p[j-1][0]) +abs(y-p[j-1][1]) )
            if Minnn>temp2:
                Minnn=temp2
            temp=temp+Minnn
        if temp<Minn:
            Minn=temp
        
    else:
        for i in range(s,PCount+1):
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
DFS(0,1)

print(Minn)

# from itertools import combinations
# arr=[[1,2],[2,3],[3,4]]
# print(list(combinations(arr,2)))












