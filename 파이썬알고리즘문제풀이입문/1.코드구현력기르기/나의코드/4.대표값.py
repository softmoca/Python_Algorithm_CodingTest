n=int(input())
arr=list(map(int,input().split()))

s=sum(arr)
avg=round(s/n+0.1)

res=[]
Mins=100
for i in range(n):
    if  Mins> abs(avg-arr[i]):
        Mins=abs(avg-arr[i])

for i in range(n):
    if abs(avg-arr[i])==Mins:
        res.append(i)
    
for x in res:
    if arr[x]>=avg:
        print(avg,x+1)
        break
else:
    print(avg,res[0])





