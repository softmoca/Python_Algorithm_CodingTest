n=int(input())
arr=list(map(int,input().split()))

arr.insert(0,0)
dy=[0]*(n+1)

dy[1]=1
for i in range(2,n+1):
    M=0
    for j in range(i-1,0,-1):
        
        if arr[i] >arr[j] and dy[j]>M:
            M=dy[j]
    dy[i]=M+1

print(max(dy))