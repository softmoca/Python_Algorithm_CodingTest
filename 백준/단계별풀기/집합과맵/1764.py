from collections import defaultdict

n,m=map(int,input().split())

dic=defaultdict(int)

for _ in range(n+m):
    dic[input()]+=1

cnt=0
res=[]
# for key,val in dic.items():
#     if val==2:
#         res.append(key)
#         cnt+=1

for x in dic:
    if dic[x]==2:
        cnt+=1
        res.append(x)


res.sort()
print(cnt)
for x in res:
    print(x)





