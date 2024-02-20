import sys
import heapq

n=int(input())
arr=[]
for _ in range(n):
    x=int(sys.stdin.readline())
    if x:
        heapq.heappush(arr,x)
    else:
        if len(arr)==0:
            print(0)
        else:
            print(heapq.heappop(arr))






