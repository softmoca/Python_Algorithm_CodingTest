n,c=map(int,input().split())
arr=[]

for _ in range(n):
    arr.append(int(input()))
arr.sort()
l=1
r=max(arr)
answer=[]

while l<=r:
    mid=(l+r)//2

    now=arr[0]
    cnt=1
    for i in range(1,len(arr)):

        if now + mid<=arr[i]:
            cnt+=1
            now=arr[i]
    print(mid,cnt)

    if cnt<c:
        r=mid-1
    elif cnt>=c:
        answer.append(mid)
        l=mid+1
print(answer)
print(max(answer))

    










