import sys
input = sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))

summ=0
prefix_sum=[0]
for i in arr:
    summ+=i
    prefix_sum.append(summ)

for _ in range(m):
    a,b=map(int,input().split())
    print(prefix_sum[b]-prefix_sum[a-1])






####################################

import sys
input = sys.stdin.readline
 
m, n = map(int, input().split())
arr=list(map(int,sys.stdin.readline().split()))
prefix_sum = [0]       
 
temp = 0    
for i in arr:    # accumulate arr section 
    temp += i
    prefix_sum.append(temp)
 
for i in range(n):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])



