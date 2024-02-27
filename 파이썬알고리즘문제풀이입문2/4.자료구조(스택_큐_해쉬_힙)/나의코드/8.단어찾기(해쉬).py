
from collections import defaultdict


dic=defaultdict(int)

n=int(input())

for _ in range(n):
    dic[input()]=1
for _ in range(n-1):
    dic[input()]=0

for key,val in dic.items():
    if val ==1:
        print(key)











