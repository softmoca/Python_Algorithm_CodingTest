from collections import defaultdict

n,m=map(int,input().split())

arr1=list(map(int,input().split()))

arr2=list(map(int,input().split()))
dic1=defaultdict(int)
dic2=defaultdict(int)

for x in arr1:
    dic1[x]+=1
    dic2[x]-=1
for x in arr2:
    dic1[x]-=1
    dic2[x]+=1

cnt=0
for x in dic1:
    if dic1[x]==1:
        cnt+=1

for x in dic2:
    if dic2[x]==1:
        cnt+=1
print(cnt)



