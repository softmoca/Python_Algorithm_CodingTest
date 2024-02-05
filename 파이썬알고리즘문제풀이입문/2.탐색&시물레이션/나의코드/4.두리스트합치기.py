n=int(input())
arr1=list(map(int,input().split()))

m=int(input())
arr2=list(map(int,input().split()))

p1=0
p2=0
res=[]
while True:
    if p1==n:
        res=res+arr2[p2:]
        break
    elif p2==m:
        res=res+arr1[p1:]
        break
    if arr1[p1]<arr2[p2]:
        res.append(arr1[p1])
        p1+=1
    else:
        res.append(arr2[p2])
        p2+=1

print(res)




