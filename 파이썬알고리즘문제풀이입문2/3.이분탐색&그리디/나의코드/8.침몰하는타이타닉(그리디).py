







n,m=map(int,input().split())

arr=list(map(int,input().split()))


arr.sort()
cnt=0
while arr:
    if arr[0]+arr[-1]<=m:
        arr.pop(0)
        arr.pop()
        cnt+=1
    else:
        arr.pop()
        cnt+=1

print(cnt)


