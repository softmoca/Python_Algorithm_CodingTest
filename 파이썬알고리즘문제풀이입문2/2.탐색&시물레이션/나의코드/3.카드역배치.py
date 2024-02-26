

ch=[0]*21

for i in range(21):
    ch[i]=i


for _ in range(10):
    a,b=map(int,input().split())
    N=(b-a)//2+1
    for i in range(N):
        ch[a+i],ch[b-i]=ch[b-i],ch[a+i]
    
print(ch)






