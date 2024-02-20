import sys

n,c=map(int,input().split())

arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

l=1
r=arr[-1]
res=0
while l<=r:
    mid=(l+r)//2
    cnt=1
    ep=arr[0]
    for i in range(1,n):
        if arr[i]-ep>=mid:
            cnt+=1
            ep=arr[i]
        
    if cnt>=c:
        res=mid
        l=mid+1
    elif cnt<c:
        r=mid-1

print(res)







