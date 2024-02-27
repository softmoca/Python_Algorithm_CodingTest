from collections import deque


s,e=map(int,input().split())

ch=[0]*(1000001)
dq=deque()
dq.append(5)
ch[5]=1
L=0

while dq:
    
    for _ in range(len(dq)):
        now=dq.popleft()
        if now==e:
            print(L)
            break

        for next in (now-1,now+1,now+5):
            if 1<=next<10001 and ch[next]==0:
                dq.append(next)
                ch[next]=1
    L+=1







