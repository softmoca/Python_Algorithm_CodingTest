
n,m=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()
l=0
r=len(arr)-1
while l<=r:
    mid=(l+r)//2

    if arr[mid]==m:
        print(mid+1)
        break
    elif arr[mid]<m:
        l=mid+1
    elif arr[mid]>m:
        r=mid-1











