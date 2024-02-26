



n=int(input())
arr=list(map(int,input().split()))

res=[]
if arr[0]<arr[-1]:
    res.append([arr[0],'L'])
    l=1
    r=n-1
else:
    res.append([arr[-1],'R'])
    r=n-2


for _ in range(n-1):
    if arr[l]<arr[r]:
        if res[-1][0]<arr[l]:
            res.append([arr[l],'L'])
            l+=1
        elif res[-1][0]<arr[r]:
            res.append([arr[r],'R'])
            r=r-1

    elif arr[l]>arr[r]:
        if res[-1][0]<arr[r]:
            res.append([arr[r],'R'])
            r=r-1
        elif res[-1][0]<arr[l]:
            res.append([arr[l],'L'])
            l=l+1

print(len(res))

for x in res:
    print(x[1],end='')
        





