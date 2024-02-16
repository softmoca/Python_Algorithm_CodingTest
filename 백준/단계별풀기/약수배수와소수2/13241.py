# a,b=map(int,input().split())
# res=a*b


# while b !=0:
#     r=a%b
#     a=b
#     b=r
# print(res//a)



import math

a,b=map(int,input().split())
res=a*b


g=math.gcd(a,b)
print(res//g)
