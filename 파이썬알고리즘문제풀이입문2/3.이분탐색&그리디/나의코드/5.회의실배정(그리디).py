
n=int(input())
arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])

print(arr)

arr.sort(key= lambda x: x[1])
print(arr)

start=arr[0][1]

cnt=1
for i in range(1,n):
    if arr[i][0]>=start:
        cnt+=1
        start=arr[i][1]
print(cnt)


