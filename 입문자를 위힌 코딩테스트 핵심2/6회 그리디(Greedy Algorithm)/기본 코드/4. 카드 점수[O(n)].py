def solution(nums, k):
    answer = 0
    N=len(nums)
    S=sum(nums)
    block_size=N-k

    Minn=100
    for i in range(N-block_size+1):
        if Minn>sum(nums[i:i+block_size]):
            Minn=sum(nums[i:i+block_size])
    answer=S-Minn
    

    

    return answer
        
                                         
print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))
