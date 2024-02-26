def count(mid):
    cnt=0
    tmp=mid
    for i in range(len(arr)):
        if tmp-arr[i]>=0:
            tmp=tmp-arr[i]
        else:
            cnt+=1
            tmp=mid-arr[i]
    return cnt+1

n,m=map(int,input().split())
arr=list(map(int,input().split()))
l=1
maxx=max(arr)
r=sum(arr)
answer=[]
while l<=r:

    mid=(l+r)//2
    if mid >=maxx and count(mid)<=m:
          answer.append(mid)
          r=mid-1
    else:
        l=mid+1
    
print(answer)
print(min(answer))







