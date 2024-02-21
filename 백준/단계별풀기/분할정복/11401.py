def factor(x):
    if x==1:
        return 1
    else:
        return x*factor(x-1)




n,k=map(int,input().split())

res=factor(n)//factor(n-k)//factor(k)


print(res%1000000007)



######################
# 스택 오버 플로우  ==> 페르마의 소정리 활용해야함