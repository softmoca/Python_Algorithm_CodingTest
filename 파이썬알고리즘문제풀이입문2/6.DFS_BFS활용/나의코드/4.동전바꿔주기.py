def DFS(L,summ):
    global cnt
    if summ>total:
        return

    if L==c:
        if summ==total:
            cnt+=1
    else:
        for i in range(count[L]+1):
            DFS(L+1,summ+point[L]*i)
            



total=int(input())
c=int(input())
point=[]
count=[]
cnt=0
for _ in range(c):
    a,b=map(int,input().split())
    point.append(a)
    count.append(b)


DFS(0,0)
print(cnt)







