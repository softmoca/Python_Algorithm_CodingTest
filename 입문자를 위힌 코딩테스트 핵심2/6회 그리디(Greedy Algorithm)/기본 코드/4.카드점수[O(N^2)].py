def solution(nums, k):
    answer = 0
    

    for i in range(k):
        if answer<sum(nums[:i]) + sum( nums[len(nums)-k+i:] ):
            answer=sum(nums[:i]) + sum( nums[len(nums)-k+i:] )

    

    

    return answer
        
                                         
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))











