import sys
n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

cnt=0

for i in range(n):
    if m%arr[n-i-1]==m:
        continue
    else:
        cnt=cnt+m//arr[n-i-1]
        m=m%arr[n-i-1]
    if m==0:
        break

print(cnt)
