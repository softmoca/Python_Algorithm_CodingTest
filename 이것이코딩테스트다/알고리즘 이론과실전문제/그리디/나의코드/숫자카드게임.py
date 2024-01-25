n,m=map(int, input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
res=[0]*n

for i in range(n):
    res[i]=min(arr[i])

print(max(res))