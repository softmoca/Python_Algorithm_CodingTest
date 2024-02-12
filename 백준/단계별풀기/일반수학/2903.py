n=int(input())

ch=[0]*n
ch.insert(0,2)
for i in range(1,n+1):
    ch[i]=ch[i-1]+ch[i-1]-1

print(ch[-1]*ch[-1])
