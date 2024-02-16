import sys
n=int(input())

arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))

dis=[]

for i in range(n-1):
    dis.append(arr[i+1]-arr[i])

a=dis[0]
b=dis[1]
while b !=0:
        r=a%b
        a=b
        b=r
g=a

for i in range(1,len(dis)):
    b=dis[i]
    while b !=0:
        r=g%b
        g=b
        b=r

    
cnt=0
for x in dis:
    cnt=cnt+x//g-1
print(cnt)















