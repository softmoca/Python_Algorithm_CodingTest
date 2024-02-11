def DFS(day,summ):
    
    global M
    if day>n+1:
        return
    if day==n+1:
        if M<summ:
            M=summ
    else:
        DFS(day+dayS[day],summ+PointS[day])
        DFS(day+1,summ)


n=int(input())
dayS=[0]
PointS=[0]
for _ in range(n):
    a,b=map(int,input().split())
    dayS.append(a)
    PointS.append(b)
M=0
DFS(1,0)


print(M)




