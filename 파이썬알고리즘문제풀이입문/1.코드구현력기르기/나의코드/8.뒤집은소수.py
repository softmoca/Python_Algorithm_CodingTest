
def reverse(x):
    res=0
    while x>0:
            if x%10==0:
                x=x//10
            else:
                res=res*10+x%10
                x=x//10
    return res

def isPrime(x):
     for i in range(2,x):
          if x%i==0:
               return False
     return True
               
n=int(input())

arr=list(map(int,input().split()))

for i in range(n):
    x=reverse(arr[i])
    if isPrime(x):
         print(x,end=' ')




