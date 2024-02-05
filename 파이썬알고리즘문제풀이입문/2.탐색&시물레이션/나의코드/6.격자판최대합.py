n=int(input())

arr=[list(map(int,input().split())) for _ in range(n) ]

S3=0 # 왼쪽아래 대각선
S2=0 # 오른 아래 대각선
S4=0 # 세로합
M=0

for i in range(n):
    if M<sum(arr[i]):
        M=sum(arr[i])
    S3+=arr[i][n-1-i]

for i in range(n):
    S4=0
    for j in range(n):
        if i==j:
            S2+=arr[i][j]
        S4=arr[j][i]
    if M<S4:
        M=S4

print(max(M,S3,S2))



