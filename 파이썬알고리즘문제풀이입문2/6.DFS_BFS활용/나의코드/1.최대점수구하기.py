def DFS(L,score_sum,time_sum):
    global Maxx
    if time_sum>m:
        return

    if L==n:
        if Maxx<score_sum:
            Maxx=score_sum


    else:
        DFS(L+1,score_sum+score[L],time_sum+time[L])
        DFS(L+1,score_sum,time_sum)

n,m=map(int,input().split())

score=[]
time=[]
for _ in range(n):
    a,b=map(int,input().split())
    score.append(a)
    time.append(b)
Maxx=0
DFS(0,0,0)


print(Maxx)







