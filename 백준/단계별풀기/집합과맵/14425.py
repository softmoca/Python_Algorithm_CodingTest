from collections import defaultdict

n,m=map(int,input().split())
dic=defaultdict(int)


for _ in range(n):
    dic[input()]=1

arr2=[]
for _ in range(m):
    arr2.append(input())
cnt=0
for x in arr2:
    if x in dic:
        cnt+=1
print(cnt)













