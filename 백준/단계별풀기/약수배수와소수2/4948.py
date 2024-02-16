

while True:
    n=int(input())
    if n==0:
        break
    ch=[0]*(2*n+1)

    for i in range(2,n*2+1):
        if ch[i]==0:
            for j in range(2*i,2*n+1,i):
                ch[j]=1

    cnt=0
    for i in range(n+1,2*n+1):
        if ch[i]==0:
            cnt+=1
    print(cnt)
            


