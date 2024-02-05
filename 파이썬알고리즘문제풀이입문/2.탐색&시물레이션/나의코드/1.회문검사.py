n=int(input())


for j in range(1,n+1):
    arr=input()
    temp=arr.upper()
    arr=list(temp)
    for i in range(len(arr)//2):
        if arr[i]!=arr[-(i+1)]:
            print("#%d NO" %(j))
            break
    else:
        print("#%d YES" %(j))

 



