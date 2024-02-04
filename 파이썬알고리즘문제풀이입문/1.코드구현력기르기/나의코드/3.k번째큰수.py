n,k=map(int,input().split())
arr=list(map(int,input().split()))

res=set()

for i in range(n):
    for j in range(i+1,n):
        for q in range(j+1,n):
            s=arr[i]+arr[j]+arr[q]
            res.add(s)

res=list(res)
res.sort(reverse=True)

print(res[k-1])



