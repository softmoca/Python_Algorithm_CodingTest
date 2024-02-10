def DFS(L):
    global cnt
    if L==m:
        cnt+=1
        print(ch)
    else:

        for i in range(1,n+1):
            for j in range(L):
                if ch[j]==i:
                    break
            else:
                ch[L]=i
                DFS(L+1)
          

n,m=map(int,input().split())
ch=[0]*m
cnt=0
DFS(0)

print(cnt)