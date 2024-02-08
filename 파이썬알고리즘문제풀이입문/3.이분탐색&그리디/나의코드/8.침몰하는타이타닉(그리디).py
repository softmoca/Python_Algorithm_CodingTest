n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

cnt=0
l=0
r=len(arr)-1

while arr:
    if len(arr)==1:
        cnt+=1
        arr.pop()
    elif arr[l]+arr[r] >m:
        r=r-1
    elif arr[l] + arr[r]<=m:
        arr.pop(l)
        arr.pop(r)
        l=0
        r=len(arr)-1
        cnt+=1
    
print(cnt)



