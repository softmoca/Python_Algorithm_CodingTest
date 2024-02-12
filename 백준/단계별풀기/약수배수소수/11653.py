n=int(input())

res=[]

for i in range(2,n+1):
    while n!=1:
        
        if n%i==0:
            res.append(i)
            n=n//i
        else:
            break

for x in res:
    print(x)




