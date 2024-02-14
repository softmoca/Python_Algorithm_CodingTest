from collections import defaultdict

n=int(input())

arr=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

dic=defaultdict(int)

for x in arr:
    dic[x]=1

for x in arr2:
    print(dic[x],end=' ')
