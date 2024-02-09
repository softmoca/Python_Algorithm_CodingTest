from collections import defaultdict

n=int(input())
dic=defaultdict()

for i in range(n):
    temp=input()
    dic[temp]=1

for i in range(n-1):
    temp2=input()
    dic[temp2]-=1
print()
for x in dic.keys():
    if dic[x]==1:
        print(x)




