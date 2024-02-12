
arr=[[0]*100 for _ in range(100)]

n=int(input())
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(10):
        for j in range(10):
            arr[a+i][b+j]=1

S=0
for i in range(100):
    S+=sum(arr[i])

print(S)