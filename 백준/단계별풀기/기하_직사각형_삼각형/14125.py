arr=list(map(int,input().split()))

if max(arr)< sum(arr)-max(arr):
    print(sum(arr))
else:
    while True:
        arr.sort()
        arr[2]=arr[2]-1        
        if max(arr)< sum(arr)-max(arr):
            print(sum(arr))
            break
    

  



