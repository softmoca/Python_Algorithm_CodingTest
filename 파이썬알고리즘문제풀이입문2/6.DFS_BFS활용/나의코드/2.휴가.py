def DFS(L,point_sum):
    global Maxx
    if L==n+1:
        if point_sum>Maxx:
            Maxx=point_sum
    else:
        if L+time[L]<=n+1:
            DFS(L+time[L],point_sum+point[L])
            DFS(L+1,point_sum)

n=int(input())
time=[]
point=[]
for _ in range(n):
    a,b=map(int,input().split())
    time.append(a)
    point.append(b)

time.insert(0,0)
point.insert(0,0)
Maxx=0
DFS(1,0)
print(Maxx)
