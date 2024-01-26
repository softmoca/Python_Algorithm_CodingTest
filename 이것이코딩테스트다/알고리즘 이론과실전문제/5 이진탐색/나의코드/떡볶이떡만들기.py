n,m=map(int,input().split())

arr=list(map(int,input().split()))

MM=0

left=0
right=max(arr)

while left<=right:
    mid=(left+right)//2
    temp=0
    for x in arr:
        if x-mid>0:
            temp+=(x-mid)
    if temp>=m :
        left=mid+1
        MM=mid
    elif temp<m:
        right=mid-1
print(MM)




