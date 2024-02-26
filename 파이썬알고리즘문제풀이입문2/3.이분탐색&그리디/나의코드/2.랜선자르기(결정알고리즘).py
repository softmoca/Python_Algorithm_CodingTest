k,n=map(int,input().split())


arr=[]
for _ in range(k):
    arr.append(int(input()))

l=1
r=max(arr)
answer=[]
while l<=r:
    print(l,r)
    mid=(l+r)//2

    cnt=0

    for x in arr:
        cnt=cnt+x//mid
    
    if cnt>n:
        l=mid+1
    elif cnt<n:
        r=mid-1
    elif cnt==n:
        answer.append(mid)
        l=mid+1
print(answer)




