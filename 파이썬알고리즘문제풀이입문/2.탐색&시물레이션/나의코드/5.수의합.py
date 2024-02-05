n,m=map(int,input().split())
arr=list(map(int,input().split()))

p1=0
p2=1
cnt=0

while p1<n and p2 <n+1 :
    if m>sum(arr[p1:p2]):
        p2+=1
    elif m<sum(arr[p1:p2]):
        p1+=1
    elif m==sum(arr[p1:p2]):
        if p2==n:
            cnt+=1
            p1+=1
        else:
            cnt+=1
            p2+=1
print(cnt)


    
 
    







