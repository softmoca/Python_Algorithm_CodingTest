def solution(nums):
    answer = 0

    N=len(nums)

    res=set(nums)
  
            
    return N//2 if len(res)>=N//2 else len(res)
    
                       
print(solution([2, 1, 1, 3, 2, 3, 1, 2]))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solution([100, 200, 300, 400, 500, 600, 700, 800]))
