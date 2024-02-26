

n=int(input())
res=[]

arr=[list(map(int,input().split())) for _ in range(n) ]


for i in range(n):
   res.append(sum(arr[i]))





for i in range(n):
    sum_row=0 # 열의 합
    for j in range(n):
        sum_row=sum_row+arr[j][i]
    res.append(sum_row)


res.append(sum_row)

sum_1=0 # 왼쪽 아래 대각

for i in range(n):
    sum_1=sum_1+arr[i][n-i-1]

res.append(sum_1)


sum_2=0 # 오른쪽 아래 대각

for i in range(n):
    sum_2=sum_2+arr[i][i]

res.append(sum_2)
print(max(res))

print(res)