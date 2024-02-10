def DFS(n):
    if n==0:
        S=0
        for i in range(len(ch)):
            if ch[i]==1:
                S=S+arr[i]

        if (S==sum(arr)-S):
            print(S,sum(arr))
            print("Yes")
            print(ch)
       
    else:
        ch[n]=1
        DFS(n-1)
        ch[n]=0
        DFS(n-1)


n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
ch=[0]*(n+1)
DFS(n)

