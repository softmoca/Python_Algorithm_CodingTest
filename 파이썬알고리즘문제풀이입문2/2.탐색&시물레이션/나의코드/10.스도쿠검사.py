
arr=[list(map(int,input().split())) for _ in range(9)]

# 행 체크
for i in range(9):
    ch=[0]*10
    flag=0
    for j in range(9):
        ch[arr[i][j]]=1
    if sum(ch)!=9:
        flag=1
        break

# 열체크
for i in range(9):
    ch=[0]*10
    flag2=0
    for j in range(9):
        ch[arr[j][i]]=1
    if sum(ch)!=9:
        flag2=1
        break

# 3x3체크
    

for i in range(0,7,3):
    for j in range(0,7,3):
        ch=[0]*10
        flag3=0
        for k in range(3):
            for w in range(3):
                ch[arr[i+k][j+w]]=1
        if sum(ch)!=9:
            flag3=1
            break;


if flag==1 or flag2 == 1 or flag3 ==1:
    print("NO")
else:
    print("YES")
        







