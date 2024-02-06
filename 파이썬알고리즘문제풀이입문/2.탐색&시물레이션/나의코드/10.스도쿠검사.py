import sys

arr=[list(map(int,input().split())) for _ in range(9) ]


ch1=[0]*10 # 가로
ch2=[0]*10 # 세로
ch3=[0]*10 # 3x3


for i in range(9):
    ch1=[0]*10 # 가로
    ch1[0]=1
    ch2=[0]*10 # 세로
    ch2[0]=1
    for j in range(9):
        ch1[arr[i][j]]+=1
        ch2[arr[j][i]]+=1

    for x in ch1:
        if x==0:
             print("No")
             sys.exit()
    for x in ch2:
        if x==0:
             print("No")
             sys.exit()

for k in range(3):
    for w in range(3):
        ch3=[0]*10 # 3x3
        ch3[0]=1
        for i in range(3):
            for j in range(3):
                ch3[arr[i+3*k][j+3*w]]+=1
        for x in ch2:
            if x==0:
                print("No")
                sys.exit()
print("YES")





