from collections import deque

n,m=map(int,input().split())
arr=list(input().split())
cnt=0
dq=deque()

for x,y in enumerate(arr):
    dq.append([x,int(y)])

while True:
    M=0
    for i in range(len(dq)):
        if M<dq[i][1]:
            M=dq[i][1]
    
    if dq[0][1]==M:
        print(dq,M,cnt)
        if dq[0][0]==m:
            print(cnt+1)
            break
        dq.popleft()
        cnt+=1
        
    elif dq[0][1] !=M:
        dq.append(dq.popleft())
