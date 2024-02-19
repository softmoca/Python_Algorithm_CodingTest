import sys
n=int(input())

arr=[]
for _ in range(n):
    a,b=map(int,sys.stdin.readline().split())
    arr.append([a,b])

arr.sort(key= lambda x:x[1])
print(arr)
arr.sort(key= lambda x:(x[1], x[0]))
print(arr)
cnt=1
end=arr[0][1]
for i in range(1,n):
    if arr[i][0]>=end:
        cnt+=1
        end=arr[i][1]

print(cnt)
