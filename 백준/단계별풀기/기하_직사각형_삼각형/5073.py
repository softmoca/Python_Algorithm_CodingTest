while True:
    arr=list(map(int,input().split()))


    if arr[0]==0 and arr[1]==0 and arr[2]==0:
        break
    arr.sort()
    if arr[0] != arr[1] and arr[1] != arr[2] and arr[0] != arr[2]:
        if arr[2]>= arr[1]+arr[0]:
            print("Invalid")
        else:
            print("Scalene")
    elif arr[0]==arr[1] and arr[1]==arr[2]:
        print("Equilateral")

    
    else: 
        print("Isosceles")
    
    
 
        





