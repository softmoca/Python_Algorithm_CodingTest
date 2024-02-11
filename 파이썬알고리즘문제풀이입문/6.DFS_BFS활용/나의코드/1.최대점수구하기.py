
def DFS(L,PointS,TimeS):
    global M
    if TimeS>m:
        return

    if L==n:
        if PointS>M:
            M=PointS
    else:
        DFS(L+1,PointS+arr[L][0],TimeS+arr[L][1])
        DFS(L+1,PointS,TimeS)

n,m=map(int,input().split())

arr=[]

for _ in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])
M=0

DFS(0,0,0)



print(M)

