n,m=map(int,input().split())

coin=[]
for i in range(n):
    coin.append(int(input()))

dy=[10001]*(m+1)
dy[0]=0
for i in range(n):
    for j in range(coin[i],m+1):
        dy[j]=min(dy[j],dy[j-coin[i]]+1)

if dy[m]==10001:
    print(-1)
else:
    print(dy[m])






