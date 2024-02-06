n,m=map(int,input().split())
arr=[]

for _ in range(n):
    arr.append(int(input()))

l=1
r=max(arr)
M=0
while l<r:
    mid=(l+r)//2
    cnt=0

    for x in arr:
        cnt+=(x//mid)
    
    if cnt<m:
        r=mid-1
    elif cnt>m:
        l=mid+1
    elif cnt==m:
        if M<mid:
            M=mid
        l=mid+1
print(M)






