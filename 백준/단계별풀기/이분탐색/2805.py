n,m=map(int,input().split())

arr=list(map(int,input().split()))

l=0
r=max(arr)
res=0
while l<=r:
    mid=(l+r)//2
    cnt=0
    for x in arr:
        if x>=mid:
            cnt=cnt+x-mid

    if cnt>=m:
        res=mid
        l=mid+1
    elif cnt<m:
        r=mid-1


print(res)









