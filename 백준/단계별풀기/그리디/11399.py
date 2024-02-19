
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
summ=arr[0]
arr2=[arr[0]]
for i in range(1,n):
    summ=summ+arr[i]
    arr2.append(summ)


print(sum(arr2))








