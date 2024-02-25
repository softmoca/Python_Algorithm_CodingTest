from collections import deque

def solution(home):
    answer = 0
    
    ch=[0]*10001

    dq=deque([0])
    L=0
    ch[0]=1
    while dq:
        for _ in range(len(dq)):
            x=dq.popleft()
            if x==home:
                answer=L
                return answer
            for next in (x-1,x+1,x+5):
                if 0<=next<=10000 and ch[next]==0:
                    dq.append(next)
                    ch[x]=1
        L+=1



    
            
print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))
