n=int(input())

ch=[1]*(n+1)
cnt=0
ch[0]=0
ch[1]=0

for i in range(2,n+1):
    if ch[i]==1:
        for j in range(2,n+1):
            if i*j >n:
                break
            ch[i*j]=0

print(sum(ch))

