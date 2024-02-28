from itertools import combinations



n,m=map(int,input().split())


arr=list(map(int,input().split()))

q=[]

res=list(combinations(arr,3))
M=0

for x in res:
    if M<sum(x) and sum(x)<=m:
        M=sum(x)
print(M)
