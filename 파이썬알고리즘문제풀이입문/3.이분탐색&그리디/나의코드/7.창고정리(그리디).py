L=int(input())
arr=list(map(int,input().split()))
M=int(input())

arr.sort(reverse=True)

for _ in range(M):
    arr[0]-=1
    arr[-1]+=1
    arr.sort(reverse=True)

print(arr[0]-arr[-1])









