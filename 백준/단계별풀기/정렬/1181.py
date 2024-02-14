n=int(input())

arr=[]
for _ in range(n):
    arr.append(input())

arr=list(set(arr))



arr.sort()
arr.sort(key=len)


for x in arr:
    print(x)

