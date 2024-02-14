n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.sort(key=lambda x: (x[1],x[0]))

for x in arr:
    print(x[0],x[1])
