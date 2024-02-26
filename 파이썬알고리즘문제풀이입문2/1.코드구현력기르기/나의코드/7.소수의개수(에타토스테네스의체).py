n=int(input())


ch=[1]*(n+1)
ch[0]=0
ch[1]=0


for i in range(2,int(n**0.5)+1):
    if ch[i]==1:
        for j in range(i*i,n+1,i):
            ch[j]=0

print(sum(ch))







