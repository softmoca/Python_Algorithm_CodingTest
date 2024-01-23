from collections import deque

def solution(home):
    answer = 0
    dq=deque()
    dq.append(0)
    L=0
    while dq:
        n=len(dq)
        for x in range(n):
            v=dq.popleft()
            for nv in [v-1,v+1,v+5]:
                if nv>=0 and nv <= 10000:
                    if nv ==home:
                        return L+1
                    dq.append(nv)
        L+=1
            
    return answer
            
print(solution(10))
print(solution(14))
print(solution(25))
print(solution(24))
print(solution(345))
