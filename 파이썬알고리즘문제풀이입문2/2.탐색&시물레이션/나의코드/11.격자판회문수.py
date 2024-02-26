arr=[list(map(int,input().split())) for _ in range(7)]

cnt=0
for i in range(7):
    for j in range(3):
        temp=arr[i][j:j+5]
        flag1=0
        for k in range(2):
            if temp[k]==temp[-(k+1)]:
                continue
            else:
                flag1=1
        if flag1==0:
            print(temp)
            cnt+=1
            
 
for i in range(7):
    for j in range(3):
        flag=0
        for k in range(2):
            if arr[j+k][i]==arr[j+4-k][i]:
                continue
            else:
                flag=1
        if flag==0:
            cnt+=1



print(cnt)

