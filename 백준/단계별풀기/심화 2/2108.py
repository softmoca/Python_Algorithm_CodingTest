


import sys
from collections import defaultdict
n=int(input())
arr=[]
dic=defaultdict(int)
for _ in range(n):
    x=sys.stdin.readline().rstrip()
    arr.append(int(x))
    dic[x]+=1


print(round(sum(arr)/n))
arr.sort()
print(arr[n//2])

freq=max(dic.values())

num=[]
for key,val in  dic.items():
    if val ==freq:
        num.append(int(key))
num.sort()

if len(num)==1:
    print(num[0])
else:
    print(num[1])



print(max(arr)-min(arr))



