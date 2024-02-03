n=int(input())

arr=[]
in_count=[]

for i in range(0,n):
    arr.append(list(map(int,input().split())))
    arr[i].pop()
    in_count.append(len(arr[i])-1)


for x in arr:
    if len(x)==1:
        print(x[0])
    else:
        S=x[0]
        for i in range(1,len(x)):
            S=S+arr[x[i]][0]
            print(S)
        print(S)









