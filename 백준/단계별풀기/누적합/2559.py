import sys
n,k=map(int,input().split())

arr=list(map(int,input().split()))

summ=[]

for i in range(n-k+1):
    summ[i]=sum(arr[i:i+k])
print(max(summ))
##################################
import sys
input = sys.stdin.readline

n, k = map(int,input().split())
arr = list(map(int, input().split()))

result = []
result.append(sum(arr[:k]))

for i in range(n - k):
    result.append(result[i] - arr[i] + arr[k+i])
        
print(max(result))




