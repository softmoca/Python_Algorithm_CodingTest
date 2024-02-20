import sys
import heapq

arr=[]
n=int(input())
for _ in range(n):
    x=int(sys.stdin.readline())
    if x:
        heapq.heappush(arr,-x)
    else:
        if len(arr)>=1:
            print(-heapq.heappop(arr))
        else:
            print(0)





