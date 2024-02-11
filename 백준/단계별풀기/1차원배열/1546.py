n=int(input())

arr=list(map(int,input().split()))
M=max(arr)
S=0
for i in range(n):
    arr[i]=arr[i]/M*100
    S+=arr[i]
avg=S/n
print(avg)





