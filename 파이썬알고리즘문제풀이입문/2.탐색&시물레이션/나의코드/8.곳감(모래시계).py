n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

m=int(input())

for i in range(m):
    a,b,c=map(int,input().split())
    for _ in range(c):
        if b==0:
            arr[a-1].append(arr[a-1].pop(0))
        elif b==1:
            arr[a-1].insert(0,arr[a-1].pop())

SSS=0
s=0
e=n
for i in range(n): 
    for j in range(s,e):
        SSS+=arr[i][j]
    if i<n//2:
        s+=1
        e-=1
    elif i>=n//2:
        s-=1
        e+=1
    
print(SSS)







