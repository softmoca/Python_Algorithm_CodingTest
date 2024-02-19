import sys
from collections import defaultdict
n,m=map(int,input().split())
dic=defaultdict(int)
for _ in range(n):
    x=sys.stdin.readline().rstrip()
    if len(x)>=m:
        dic[x]+=1

dic2=sorted(dic.items(),key= lambda x: (-x[1],-len(x[0]),x[0]))

for x in dic2:
    print(x[0])




