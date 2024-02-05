s=list(map(str,input()))
NUM=[]
res=0
for i in range(len(s)):
    if s[i].isdecimal():
        res=res*10+int(s[i])
        
cnt=0

for i in range(1,res+1):
    if res%i==0:
        cnt+=1

print(res,cnt)








