def Count_DVD(mid):
    cnt=0
    M=mid

    for i in range(n):
        
        M=M-arr[i]
        if M<0:
            cnt+=1
            M=mid
            M=M-arr[i]
        elif M==0:
            if i==n-1:
                cnt -=1
            cnt+=1
            M=mid
        print(M,i,arr[i],cnt)
 
    return cnt+1


n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

l=1
r=sum(arr)
SS=1000
while l<=r:
    mid=(l+r)//2

    CC=Count_DVD(mid)
    #print(l,mid,r,CC)
    if CC>m:
        l=mid+1
    elif CC<=m:
        print(l,mid,r,CC)
        if SS>mid:
            SS=mid
        r=mid-1
   

print(SS)
#print(Count_DVD(23))


