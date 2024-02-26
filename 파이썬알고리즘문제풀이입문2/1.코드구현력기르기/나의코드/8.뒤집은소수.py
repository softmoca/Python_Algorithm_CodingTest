def reverse(x):
    res=0

    while x>0:
        tmp=x%10
        x=x//10
        res=res*10+tmp

    return res


def isPrime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True





n=int(input())
res=[]
arr=list(map(int,input().split()))

for x in arr:
    reverse_Num=reverse(x)
    
    if isPrime(reverse_Num):
        res.append(reverse_Num)


print(res)




