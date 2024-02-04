n,m=map(int,input().split())
arr=[0]*(n+m+1)

for i in range(1,n+1):
    for j in range(1,m+1):
        arr[i+j]+=1
M=max(arr)
res=[]

for i in range(2,n+m+1):
    if arr[i]==M:
        res.append(i)
print(res)




