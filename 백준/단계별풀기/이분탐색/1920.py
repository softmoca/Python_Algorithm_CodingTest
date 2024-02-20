n= int(input())
arr=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))
arr.sort()


for i in range(m):
    l= 0
    r=n-1
    while l<=r:
       
        mid=(l+r)//2
    
        if arr2[i]==arr[mid]:
            print(1)
            break
        elif arr2[i] <arr[mid]:
            r=mid-1
        elif arr2[i]>arr[mid]:
            l=mid+1
        
    else:
        print(0)
 


    










