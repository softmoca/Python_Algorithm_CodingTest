N=int(input())

cnt=0
for k in range(N+1):
    if k==3 or k==13 or k==23:
        cnt+=3600
        continue
    for i in range(60):
        if i %10==3 or i//10==3:
            cnt+=60
            continue
        for j in range(60):
            if j%10==3 or j//10==3:
                cnt+=1

print(cnt)
