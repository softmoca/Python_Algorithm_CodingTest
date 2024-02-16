# from collections import deque
# dq=deque()
# n=int(input())

# arr=list(map(int,input().split()))
# for idx,val in enumerate(arr):
#     dq.append([idx+1,val])

# x=dq.popleft()[1]
# res=[1]

# while dq:
#     if x>0:
#         for _ in range(x-1):
            
#                 dq.append(dq.popleft())
#         if dq:
#             xx,yy=dq.popleft()    
#             x=yy
#             res.append(xx)
#     if x<0:
#         for _ in range(-1-x):
            
#                 dq.appendleft(dq.pop())
#         if dq:
#             xx,yy=dq.pop()
#             x=yy
#             res.append(xx)

# for x in res:
#     print(x,end=' ')

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, ans)))





