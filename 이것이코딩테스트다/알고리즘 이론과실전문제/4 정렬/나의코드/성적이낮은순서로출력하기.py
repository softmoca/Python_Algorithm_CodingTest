N=int(input())

arr=[]
for i in range(N):
    arr.append(list(map(str,input().split())))
    arr[i][1]=int(arr[i][1])

arr.sort(key=lambda x:x[1])

for i in range(N):
    print(arr[i][0], end=' ')


