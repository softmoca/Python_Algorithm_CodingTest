def solution(nums):
    answer = 0
    countt=0
    M=0
    for x in nums:
       
        if x==1:
            countt+=1
            M=countt
        elif x==0:
            countt=0
        if M>answer:
           answer=M
    return answer

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))
