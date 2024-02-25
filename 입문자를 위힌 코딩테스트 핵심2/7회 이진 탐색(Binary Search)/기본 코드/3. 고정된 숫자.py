def solution(nums):
    answer = -1

    l=0
    r=len(nums)-1

    while l<=r:
        mid=(l+r)//2

        if nums[mid]==mid:
            answer=mid
            break
        elif nums[mid]<mid:
            l=mid+1
        elif nums[mid]>mid:
            r=mid-1


    
    
    return answer    
     
    
print(solution([-3, -2, 0, 1, 3, 5, 8, 9, 12]))
print(solution([-10, -5, -2, 3, 4, 6, 7, 8]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution([-5, -3, 0, 1, 2, 3, 4, 7]))
print(solution([0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))  
