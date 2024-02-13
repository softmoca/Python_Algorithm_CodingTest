n=int(input())
y=[]
x=[]

for _ in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)

SS=(max(y)-min(y))*(max(x)-min(x))

if n==1:
    print(0)
else:
    print(SS)



