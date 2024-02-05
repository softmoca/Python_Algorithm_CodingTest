n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
S=0

for i in range(n//2+1):
    S+=sum(arr[i][n//2-i:n//2+1+i])
for i in range(n//2+1,n):
    S+=sum(arr[i][n//2+i-(n-1):n//2-i+(n)])

print(S)

