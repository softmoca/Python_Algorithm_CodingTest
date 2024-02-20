import sys
import heapq

n=int(input())
arr=[]
for _ in range(n):
    x=int(sys.stdin.readline())
    if x:
        heapq.heappush(arr,(abs(x),x))
    else:
        if len(arr)==0:
            print(0)
        else:
            y=heapq.heappop(arr)
            print(y[1])






