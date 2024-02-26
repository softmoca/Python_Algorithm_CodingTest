

n,m=map(int,input().split())

ch=[0]*(n+m+2)

for i in range(1,n+1):
    for j in range(1,m+1):
        ch[i+j]+=1
MM=max(ch)
res=[]
for i in range(2,n+m+1):
    if ch[i]==MM:
        res.append(i)
res.sort()
print(res)






