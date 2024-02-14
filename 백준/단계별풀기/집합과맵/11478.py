from collections import defaultdict

dic=defaultdict()
s=input()

n=len(s)



for i in range(1,n+1):
    for j in range(n+1-i):
        dic[s[j:i+j]]=1
cnt=0
for x in dic:
    cnt+=1
print(cnt)