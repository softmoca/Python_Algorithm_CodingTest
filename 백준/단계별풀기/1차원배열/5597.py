ch=[0]*31

for _ in range(28):
    x=int(input())
    ch[x]=1


for i in range(1,31):
    if ch[i]==0:
        print(i)