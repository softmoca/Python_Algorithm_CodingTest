from collections import defaultdict

arr1=list(input())

arr2=list(input())

dic=defaultdict(int)

for x in arr1:
    if dic[x]:
        dic[x]+=1
    else:
        dic[x]=1
print(dic)
for x in arr2:
    if dic[x]:
        dic[x]-=1
    else:
        dic[x]=-1
print(dic)
for x,y in dic.items():
    if y==1:
        print("No")
        break
else:
    print("YES")


