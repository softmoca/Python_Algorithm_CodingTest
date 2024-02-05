
n=int(input())
M=0
for i in range(n):
    a,b,c=map(int,input().split())
    if a==b and b==c:
        res=10000+a*1000
    elif a==b or b==c:
        res=1000+b*100
    elif a==c:
        res=1000+b*100
    else:
        res=max(a,b,c)*100
    if M<res:
        M=res
        
print(M)

