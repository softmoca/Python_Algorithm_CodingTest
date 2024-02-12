arr=[list(map(int,input().split())) for _ in range(9)]
M=0
a,b=0,0
for i in range(9):
    for j in range(9):
        if arr[i][j]>M:
            M=arr[i][j]
            a,b=i,j
print(M)
print(a+1,b+1)

