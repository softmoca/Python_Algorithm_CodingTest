n=int(input())


for i in range(1,n+1):
    t=i
    S=i
    while i>0:
        S=S+i%10
        i=i//10
    if S==n:
        print(t)
        break
else:
    print(0)
        
    







