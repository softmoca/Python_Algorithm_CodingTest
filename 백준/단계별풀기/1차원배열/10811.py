n,m=map(int,input().split())
arr=list(range(n+1))
for _ in range(m):
    i,j=map(int,input().split())
    for k in range((j-i)//2+1):
        arr[i+k],arr[j-k]=arr[j-k],arr[i+k]



for i in range(1,n+1):
    print(arr[i],end=' ')