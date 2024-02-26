

s=input()
res=[]
for x in s:
    if x.isnumeric():
        res.append(x)

answer=int(''.join(res))
cnt=0
for i in range(1,answer+1):
    if answer%i==0:
        cnt+=1

print(answer)

print(cnt)