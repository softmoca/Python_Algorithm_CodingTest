import heapq

q=[]

while True:
    x=int(input())
    if x==-1:
        break
    if x==0:
        if q:
            print(heapq.heappop(q))
        else:
            print(-1)
    else:
        heapq.heappush(q,x)












