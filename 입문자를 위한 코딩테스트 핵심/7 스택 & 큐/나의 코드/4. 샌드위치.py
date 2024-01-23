def solution(nums):
    answer = 0
    stack=[]

    for x in nums:
        if len(stack)>1 and stack[-1]==2 and stack[-2]==1 and x==1:
            stack.pop()
            stack.pop()
            answer+=1
        else:
            stack.append(x)

    
    return answer
    

print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
print(solution([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
print(solution([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
print(solution([2, 1, 1, 1, 2, 1, 2]))
print(solution([1, 1, 1, 1, 1, 1, 1]))
