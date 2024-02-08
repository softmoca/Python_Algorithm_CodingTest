arr,m=list(map(str,input().split()))
res=[]
m=int(m)

for x in arr:
    res.append(int(x))

M=max(res[0:m])

for _ in range(m):
    if res[0]<M:
        res.pop(0)
        m=m-1
cnt=0
for j in range(m):
    for i in range(j,len(res)-1):
        if res[i]<res[i+1]:
            res.insert(0,res.pop(i))
            m=m-1
            cnt+=1
            break

for _ in range(cnt):
    res.pop(0)

for _ in range(m):
    res.pop()

for x in res:
    print(x,end='')


    






