n=int(input())
arr=list(map(int,input().split()))

arr.insert(0,0)
ch=[0]*(n+1)

for i in range(1,n+1):
    for j in range(n+1):
        if ch[j]


        if ch[j]==0:
            ch[j]=i
            break

print(ch)




