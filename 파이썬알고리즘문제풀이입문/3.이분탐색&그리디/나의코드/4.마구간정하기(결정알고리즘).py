n,c=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(input()))

arr.sort()


l=2
r=max(arr)
res=0
while l<=r:
    cnt=1
    mid=(l+r)//2
    start=arr[0]
    for i in range(n-1):
        if (arr[i+1]-start) <mid:
            continue
        elif (arr[i+1]-start) >=mid:
            cnt+=1
            start=arr[i+1]
        
    if cnt <c:
        r=mid-1
    elif cnt>=c:
        l=mid+1
        res=mid
    

print(res)
 




