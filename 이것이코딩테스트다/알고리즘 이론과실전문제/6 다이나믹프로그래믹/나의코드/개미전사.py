N=int(input())
arr=list(map(int,input().split()))

arr.append(0)
dy=[0]*(N+1)
dy[1]=1
dy[2]=max(arr[0],arr[1])
for i in range(3,N+1):
    dy[i]=max(dy[i-1],max(dy[:i-1])+arr[i-1])

print(dy[4])




