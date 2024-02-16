
x=int(input())

ch=[0]*(n+1)
for i in range(2,int(n**0.5)+1):
    if ch[i]==0:
        for j in range(i*2,n+1,i):
            ch[j]=1

for _ in range(x):
    n=int(input())
  
    cnt=0
    for i in range(2,n//2+1):
        if ch[i]==0 and ch[n-i]==0:
            cnt+=1
    print(cnt)












