def digit_sum(x):
    s=0
    while x>0:
        s+=x%10
        x=x//10
    return s

n=int(input())
arr=list(map(int,input().split()))
res=0
M=0
for x in arr:
    if M < digit_sum(x):
        M=digit_sum(x)
        res=x
print(res)




