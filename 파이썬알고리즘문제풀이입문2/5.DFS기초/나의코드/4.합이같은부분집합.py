def DFS(x,ch):
    global Flag
    if x==n:
        s=0
        for i in range(n):
             if ch[i]==1:
                s=s+arr[i]
        if summ-s==s:
            Flag=1
        return
    else:

            ch[x]=1
            DFS(x+1,ch)
            ch[x]=0
            DFS(x+1,ch)


n=int(input())
arr=list(map(int,input().split()))
Flag=0

ch=[0]*n
summ=sum(arr)
DFS(0,ch)

if Flag ==1:
     print("YES")
else:
     print("NO")







