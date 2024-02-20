import sys
n = int(input())
arr = list(map(int, input().split()))
arr.sort()

l = 0
r = n-1

answer = 1e11

while l < r:
    sum = arr[l] + arr[r]
      
    if abs(sum) < answer:
        answer = abs(sum)
        res = [arr[l], arr[r]]
        
    if sum < 0:
        l += 1
    elif sum>0:
        r -= 1
    else:
        break

print(res[0], res[1])

