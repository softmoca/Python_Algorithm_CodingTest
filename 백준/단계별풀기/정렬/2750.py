n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()

for x in arr:
    print(x[0],x[1])


