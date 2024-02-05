n=int(input())

arr=list(map(int,input().split()))

res=0
cnt=0
for i in range(n):
    if arr[i]==1:
        cnt+=1
        res+=cnt
    else:
        cnt=0

print(res)




