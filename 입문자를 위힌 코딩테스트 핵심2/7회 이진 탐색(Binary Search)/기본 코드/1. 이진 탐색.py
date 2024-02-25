def solution(nums, target):
    answer = -1

    l=0
    r=len(nums)-1
    while l<=r:
        mid=(l+r)//2

        if nums[mid]==target:
            answer=mid
            break
        elif nums[mid]<target:
            l=l+1
        elif nums[mid]>target:
            r=r-1

    

    return answer
                                                 
print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))
