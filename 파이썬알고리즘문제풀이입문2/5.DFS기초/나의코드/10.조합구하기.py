def DFS(L,s):
    global cnt

    if L==m:
        cnt+=1
        print(res)
    else:
        for i in range(s,n+1):

            res[L]=i
            DFS(L+1,i+1)



n,m=map(int,input().split())

cnt=0
res=[0]*m


DFS(0,1)
print(cnt)









