def digit_sum(x):
    summ=0
    while x>0:
        summ=summ+x%10
        x=x//10
    return summ

n=int(input())
arr=list(map(int,input().split()))

MM=0
answer=0
for x in arr:
    if MM<digit_sum(x):
        MM=digit_sum(x)
        answer=x
print(answer)










