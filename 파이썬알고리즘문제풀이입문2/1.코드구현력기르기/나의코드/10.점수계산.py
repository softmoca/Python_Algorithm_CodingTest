n=int(input())

arr=list(map(int,input().split()))
score=0
cnt=0
for x in arr:
    if x==1:
        cnt+=1
        score+=cnt
    else:
        cnt=0

print(score)






