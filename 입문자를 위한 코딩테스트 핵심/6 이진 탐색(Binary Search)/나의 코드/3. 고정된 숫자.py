def solution(nums):
    answer = -1
    left=0
    right=len(nums)

    while left<right:
        mid=(left+right)//2
        if nums[mid]<mid:
            left=mid+1
        elif nums[mid]>mid:
            right=mid-1
        elif nums[mid]==mid:
            return mid
    
    return answer    
     
    
print(solution([-3, -2, 0, 1, 3, 5, 8, 9, 12]))
print(solution([-10, -5, -2, 3, 4, 6, 7, 8]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution([-5, -3, 0, 1, 2, 3, 4, 7]))
print(solution([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  
