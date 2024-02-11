def DFS(L,sum):
    global cnt
    if sum>T:
        return
    if L==k: 
        if sum==T:
            cnt+=1
    else:
        print(L,sum)
        for i in range(count[L]+1):
            DFS(L+1,sum+money[L]*i)

T=int(input())
k=int(input())
money=[]
count=[]
for _ in range(k):
    a,b=map(int,input().split())
    money.append(a)
    count.append(b)
cnt=0

DFS(0,0)

print(cnt)
