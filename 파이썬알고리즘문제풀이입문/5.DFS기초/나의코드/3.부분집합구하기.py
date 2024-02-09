def DFS(n,ch):
    if n==0:
       for i in range(1,len(ch)):
           if ch[i]==1:
               print(i,end=' ')
       print()
    else:
        ch[n]=1
        DFS(n-1,ch)
        ch[n]=0
        DFS(n-1,ch)


n=int(input())
ch=[0]*(n+1)
DFS(n,ch)
