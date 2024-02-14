from collections import defaultdict
import sys
n=int(input())
dic=defaultdict(int)

for _ in range(n):
    a,b=map(str,sys.stdin.readline().split())
    if b=='enter':
        dic[a]+=1
    if b=='leave':
        dic[a]-=1    
res=[]

for key,val in dic.items():
    if val==1:
        res.append(key)

res.sort(reverse=True)

for x in res:
    print(x)