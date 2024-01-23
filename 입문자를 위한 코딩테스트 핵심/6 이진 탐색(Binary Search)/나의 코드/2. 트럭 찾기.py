def solution(nums, weight):
    answer = 0
    left=0
    right=len(nums)
    while left<right:
        mid=(left+right)//2
        if weight<=nums[mid]:
            right=mid
        elif weight>nums[mid]:
            left=mid+1
    if nums[-1]<weight:
        answer=-1
    else:
        answer=right

    return answer
    
     
print(solution([100, 120, 150, 160, 165, 170, 175, 180, 190, 200], 170))                                          
print(solution([200, 250, 260, 265, 275, 290, 300, 325, 350, 370], 270))
print(solution([50, 55, 60, 65, 70, 80, 80, 80, 80, 90, 90, 90], 80))
print(solution([20, 30, 40, 50, 60, 70], 90))
print(solution([10, 30, 50, 70, 80, 90, 100, 110, 120], 115))
