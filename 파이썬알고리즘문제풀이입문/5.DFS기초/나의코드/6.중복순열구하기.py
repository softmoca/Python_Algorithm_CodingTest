def DFS(L):
    global cnt
    if L==m:
        cnt+=1
        print(ch)

    else:
        for i in range(1,n+1):
            ch[L]=i
            DFS(L+1)
            
n,m=map(int,input().split())
cnt=0
ch=[0]*m

DFS(0)
print(cnt)