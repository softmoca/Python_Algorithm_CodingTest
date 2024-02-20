n=int(input())

arr=list(map(int,input().split()))
T=int(input())

arr.sort()

l=0
r=n-1

cnt=0

while l<r:
    if arr[l]+arr[r]==T:
        cnt+=1
        r=r-1
    elif arr[l]+arr[r] <T:
        l=l+1
    elif  arr[l]+arr[r] >T:
        r=r-1
print(cnt)








