
n=int(input())
arr=list(map(int,input().split()))

AVG=int(sum(arr)/n+0.5)

Minn=1000
for x in arr:
    if abs(x-AVG)<Minn:
        Minn=abs(x-AVG)
res=[]

for i in range(n):
    if abs(arr[i]-AVG)==Minn:
        res.append([i,arr[i]])

res1=[]
for idx,val in res:
    if val>=AVG:
        res1.append([idx,val])

if res1:
    print(AVG,res1[0][0]+1)
else:
    print(AVG,res[0][0])


