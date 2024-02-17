from collections import defaultdict


n=int(input())

dic=defaultdict()
summ=0
for _ in range(n):
    x=input()
    if x=='ENTER':
      summ=summ+len(dic)
      dic=defaultdict()

    else:
       dic[x]=1
summ=summ+len(dic)

print(summ)







