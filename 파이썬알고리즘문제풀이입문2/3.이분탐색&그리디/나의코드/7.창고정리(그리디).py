




l=int(input())
arr=list(map(int,input().split()))
m=int(input())



for _ in range(m):
    arr.sort()
    arr[-1]-=1
    arr[0]+=1
print(max(arr)-min(arr))








