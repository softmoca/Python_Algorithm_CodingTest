from collections import defaultdict
n,m=map(int,input().split())
dic=defaultdict()

for i in range(1,n+1):
    x=input()
    dic[x]=i
    dic[i]=x

arr=[]
for _ in range(m):
    arr.append(input())


for x in arr:
    if x.isdecimal():
        print(dic[int(x)])
    else:
        print(dic[x])






