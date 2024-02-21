

T=int(input())

dy=[0]*(101)

dy[1]=1
dy[2]=1
dy[3]=1


for i in range(4,101):
    dy[i]=dy[i-3]+dy[i-2]

for _ in range(T):
    x=int(input())
    print(dy[x])











