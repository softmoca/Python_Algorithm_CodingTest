from collections import defaultdict

n=int(input())
dic=defaultdict(int)
arr=list(map(int,input().split()))
for x in arr:
    dic[x]+=1

m=int(input())
arr2=list(map(int,input().split()))

for x in arr2:
    print(dic[x],end=' ')
    



