n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
res=list(set(arr1+arr2))
res.sort()
print(res)


