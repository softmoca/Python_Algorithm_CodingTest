while True:
    n=int(input())
    if n==-1:
        break
    res=[]
    S=0
    for i in range(1,n):
        if n%i==0:
            res.append(i)
            S+=i
    if S==n:
        print(n,end=' ')
        print("=",end=' ')
        print(res[0],end=' ')
        for i in range(1,len(res)):
            print("+",res[i],end=' ')

        

    else:
        print("%d is NOT perfect." %(n))

    

    




