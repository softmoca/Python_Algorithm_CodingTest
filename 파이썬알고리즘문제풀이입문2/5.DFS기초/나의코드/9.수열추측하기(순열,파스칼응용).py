def DFS(L):
    global answer
    if L==n:
        s=0
        
        for i in range(n):
            s=s+(res[i]*mm[i])
 
        if s==f:
            
            tmp=[]
            for x in res:
                tmp.append(x)

            answer.append(tmp)
            

    else:
        for i in range(1, n+1):
            if ch[i]==0:
                ch[i]=1
                res[L]=i
                DFS(L+1)
                ch[i]=0


answer=[]
n,f=map(int,input().split())
mm=[0]*n
mm[0]=1
mm[-1]=1

for i in range(1,n):
    mm[i]=mm[i-1]*(n-i)//i

res=[0]*n
ch=[0]*(n+1)

DFS(0)


print(answer)

