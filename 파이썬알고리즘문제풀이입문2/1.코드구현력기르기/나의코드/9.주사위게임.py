n=int(input())
res=[]
for _ in range(n):

    a,b,c=map(int,input().split())
    if a==b and b==c:
        res.append(10000+a*1000)
    elif a==b or b==c:
        res.append(1000+b*100)
    elif a==c:
        res.append(1000+a*100)
    else:
        res.append(max(a,b,c)*100)

print(max(res))







