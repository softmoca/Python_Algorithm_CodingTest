n,m,k=map(int,input().split())

arr=list(map(int,input().split()))
arr.sort(reverse=True)

s=0
cnt=0


while True: 
    for _ in range(k):
        if cnt==m:
            print(s)
            break
        s+=arr[0]
        cnt+=1
     
    if cnt==m:
            print(s)
            break

    s+=arr[1]
    cnt+=1
    






