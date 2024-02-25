from collections import deque
def solution(nums):
    answer = 0
    dq=deque(nums)
    while dq:
        if len(dq)==1:
                answer=dq.popleft()
                break
        for _ in range(2):
            if len(dq)==1:
                answer=dq.popleft()
                break
            else:
                if dq:
                    dq.popleft()
        if dq:       
            dq.append(dq.popleft())



    return answer
            
print(solution([3, 1, 4, 5, 2, 6, 7]))
print(solution([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solution([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))
