from collections import defaultdict


dic=defaultdict(int)

s1=input()
s2=input()


for x in s1:
    dic[x]+=1

for x in s2:
    dic[x]-=1

print(dic)



for key,val in dic.items():
    if val !=0:
        print("NO")
        break
else:
    print("YES")










