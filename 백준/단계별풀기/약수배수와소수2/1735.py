n1,n2=map(int,input().split())
m1,m2=map(int,input().split())

a=m2*n1+m1*n2
b=n2*m2
res1=a
res2=b

while b!=0:
    r=a%b
    a=b
    b=r

c=res1//a
d=res2//a
print(c,d)
