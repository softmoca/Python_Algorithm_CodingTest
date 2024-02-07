n=int(input())
arr=[]

for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key = lambda x:-x[0])

cnt=1
for i in range(1,n):
    for j in range(i-1,-1,-1):
        Flag=0
        if arr[i][1]<=arr[j][1]:
            Flag=1
            break
        else:
            continue
    if Flag==0:
        cnt+=1

print(cnt)
