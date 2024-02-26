

n=int(input())
arr=[]

for _ in range(n):
    a,b=map(int,input().split())
    arr.append([a,b])

arr.sort(key= lambda x:-x[0])

cnt=1

for i in range(1,n):
    for j in range(i-1,-1,-1):
        if arr[i][1]<arr[j][1]:
            break
        else:
            continue
    else:
        cnt+=1
print(cnt)









