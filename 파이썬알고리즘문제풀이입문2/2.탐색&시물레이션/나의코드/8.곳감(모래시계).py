
n=int(input())

arr=[list(map(int,input().split())) for _ in range(n)]

m=int(input())


for _ in range(m):
    a,b,c=map(int,input().split())
    if b==1:#오른쪾
        for i in range(c):
            arr[a-1].insert(0,arr[a-1].pop())
    elif b==0:
        for i in range(c):
            arr[a-1].append(arr[a-1].pop(0))

print(arr)

s,e=0,n-1
summ=0
for i in range(n):
    for j in range(s,e+1):
        print(i,j,s,e)
        summ=summ+arr[i][j]
        
    if i<n//2:
        s=s+1
        e=e-1
    else:
        s=s-1
        e=e+1
print(summ)

