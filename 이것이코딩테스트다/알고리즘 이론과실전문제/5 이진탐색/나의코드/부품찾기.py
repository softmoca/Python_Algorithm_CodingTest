n=int(input())
arr1=list(map(int,input().split()))
m=int(input())
arr2=list(map(int,input().split()))

for i in range(m):
    left=0
    right=n
    while left<=right:
        mid=(left+right)//2
        print(left,mid,right)
        if arr1[mid]==arr2[i]:
            print("yes",end=' ')
            break
        elif arr1[mid]<arr2[i]:
            left=mid+1
        else:
            right=mid-1
    else:
        print("no",end=' ')




